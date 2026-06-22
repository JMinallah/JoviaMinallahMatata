"""Code Climate CLI Tool

Scans a Python file and returns a health report with:
- total lines, blank lines, lines of code (excluding comment-only lines and docstrings)
- counts of if/elif/else/for/while
- comment ratio (percentage of lines that are comments or docstrings)
- variable assignment checks for snake_case (warn if not)

Usage:
  python3 hackathon.py path/to/target.py
"""

from __future__ import annotations

import argparse  # this import is used in the main() function for command-line argument parsing
import ast   # this import is used for parsing the Python source code into an abstract syntax tree (AST) for analysis
import io   # this import is used for creating an in-memory text stream to tokenize the source code
import json  # this import is used for formatting the output report as JSON
import os   # this import is used for checking if the specified file path exists
import re    # this import is used for regular expression matching, particularly for validating variable names and other patterns
import sys   # this import is used for system-specific parameters and functions, such as exiting the program with a status code
import tokenize  # this import is used for tokenizing the source code to identify comments and other elements for analysis
from typing import Dict, List, Set, Tuple  # this import is used for type hinting, allowing the specification of expected data types for function parameters and return values

# this function below is used to collect the line numbers of docstrings in the source code. It parses the source code into an AST and walks through the nodes to find module, function, and class definitions. 
# If a docstring is found, it calculates the range of lines it occupies and adds those line numbers to a set, which is then returned.
def _collect_docstring_line_ranges(source: str) -> Set[int]:
	"""Return set of line numbers occupied by module/function/class docstrings."""
	doc_lines: Set[int] = set()
	try:
		tree = ast.parse(source)
	except SyntaxError:
		return doc_lines

	for node in ast.walk(tree):
		if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
			if not getattr(node, 'body', None):
				continue
			first = node.body[0]
			if isinstance(first, ast.Expr) and isinstance(getattr(first, 'value', None), ast.Constant) and isinstance(first.value.value, str):
				doc = first.value.value
				# lineno points to the start line of the docstring expression
				start = getattr(first, 'lineno', None)
				if start is None:
					continue
				n = doc.count('\n') + 1
				for ln in range(start, start + n):
					doc_lines.add(ln)
	return doc_lines

# this function is used to identify lines in the source code that are comment-only lines, meaning they start with a '#' character after stripping leading whitespace. 
# It iterates through each line of the source code, checks if it is a comment-only line, and if so, adds its line number to a set, which is then returned.
def _count_comment_only_lines(lines: List[str]) -> Set[int]:
	comment_lines: Set[int] = set()
	for i, line in enumerate(lines, start=1):
		if line.strip().startswith('#'):
			comment_lines.add(i)
	return comment_lines

# this function is used to identify lines in the source code that contain comment tokens, which may include inline comments. 
# It uses the tokenize module to generate tokens from the source code and checks for tokens of type COMMENT.
def _count_tokens_comment_lines(source: str) -> Set[int]:
	"""Find lines that contain comment tokens (may include inline comments).

	We return only lines that are pure comments here to avoid double-counting inline comments
	as comment-only lines. This function complements the simpler startswith check above.
	"""
	comment_lines: Set[int] = set()
	try:
		sio = io.StringIO(source)
		for tok in tokenize.generate_tokens(sio.readline):
			if tok.type == tokenize.COMMENT:
				lineno = tok.start[0]
				# we only mark it here; final logic will decide if it's comment-only
				comment_lines.add(lineno)
	except Exception:
		pass
	return comment_lines

# this function is used to check if a given variable name follows the snake_case naming convention. 
# It uses a regular expression to ensure that the name starts with a lowercase letter or an underscore, followed by any combination of lowercase letters, digits, or underscores. 
# If the name matches this pattern, the function returns True; otherwise, it returns False.
def _snake_case_ok(name: str) -> bool:
	return re.match(r'^[a-z_][a-z0-9_]*$', name) is not None

# this function is used to extract variable names from assignment targets in the AST. 
# It handles simple variable names, as well as tuples and lists of variables. 
# It returns a list of variable names found in the target node. 
# If the target is a simple name, it returns that name. 
# If the target is a tuple or list, it recursively extracts
def _extract_assigned_names(source: str) -> List[Tuple[str, int]]:
	names: List[Tuple[str, int]] = []
	try:
		tree = ast.parse(source)
	except SyntaxError:
		return names

	for node in ast.walk(tree):
		# simple assignments
		if isinstance(node, ast.Assign):
			for target in node.targets:
				for n in _names_from_target(target):
					names.append((n, getattr(target, 'lineno', getattr(node, 'lineno', 0))))
		elif isinstance(node, ast.AnnAssign):
			target = node.target
			for n in _names_from_target(target):
				names.append((n, getattr(target, 'lineno', getattr(node, 'lineno', 0))))
		elif isinstance(node, ast.AugAssign):
			for n in _names_from_target(node.target):
				names.append((n, getattr(node, 'lineno', 0)))
	return names

# this function is used to extract variable names from assignment targets in the AST. 
# It handles simple variable names, as well as tuples and lists of variables. 
# It returns a list of
def _names_from_target(node) -> List[str]:
	if isinstance(node, ast.Name):
		return [node.id]
	elif isinstance(node, ast.Tuple) or isinstance(node, ast.List):
		names: List[str] = []
		for elt in node.elts:
			names.extend(_names_from_target(elt))
		return names
	# ignore attributes and subscripts for variable naming rules
	return []

# this function is used to count the occurrences of control flow statements (if, elif, else, for, while) in the source code.
def _complexity_counts(source: str) -> Dict[str, int]:
	counts = {"if": 0, "elif": 0, "else": 0, "for": 0, "while": 0}
	try:
		tree = ast.parse(source)
	except SyntaxError:
		return counts

	parent: Dict[int, ast.AST] = {}

	for node in ast.walk(tree):
		for child in ast.iter_child_nodes(node):
			parent[id(child)] = node

	for node in ast.walk(tree):
		if isinstance(node, ast.If):
			# determine if this If node is an "elif" by checking whether its parent is
			# an If and it's inside parent's orelse as the first element
			p = parent.get(id(node))
			if isinstance(p, ast.If) and node in getattr(p, 'orelse', []):
				counts['elif'] += 1
			else:
				counts['if'] += 1
			# else blocks that are not elif
			if node.orelse and not (len(node.orelse) == 1 and isinstance(node.orelse[0], ast.If)):
				counts['else'] += 1
		elif isinstance(node, ast.For):
			counts['for'] += 1
		elif isinstance(node, ast.While):
			counts['while'] += 1

	return counts


def analyze_file(path: str) -> Dict:
	if not os.path.exists(path):
		raise FileNotFoundError(path)

	with open(path, 'r', encoding='utf-8') as f:
		source = f.read()

	lines = source.splitlines()
	total_lines = len(lines)
	blank_lines = sum(1 for l in lines if l.strip() == '')

	# docstring lines
	docstring_lines = _collect_docstring_line_ranges(source)

	# comment-only lines (startswith #)
	comment_only = _count_comment_only_lines(lines)

	# We consider a line comment-only if it starts with # or is part of a docstring.
	comment_only_or_doc = set(comment_only) | set(docstring_lines)

	# lines of code excluding comment-only lines and blank lines
	code_lines = total_lines - len(comment_only_or_doc) - blank_lines

	# comment ratio: percent of lines that are comments (comment-only lines + docstrings)
	comment_ratio = (len(comment_only_or_doc) / total_lines * 100) if total_lines else 0.0

	complexity = _complexity_counts(source)

	assigned = _extract_assigned_names(source)
	var_warnings: List[Dict[str, object]] = []
	for name, lineno in assigned:
		if not _snake_case_ok(name):
			var_warnings.append({"name": name, "lineno": lineno, "reason": "not snake_case"})

	result = {
		"file": path,
		"total_lines": total_lines,
		"blank_lines": blank_lines,
		"code_lines": code_lines,
		"comment_lines": len(comment_only_or_doc),
		"comment_ratio_percent": round(comment_ratio, 2),
		"complexity": complexity,
		"variable_warnings": var_warnings,
	}

	return result


def main(argv=None):
	parser = argparse.ArgumentParser(description='Code Climate CLI for a Python file')
	parser.add_argument('path', nargs='?', help='Path to Python file to analyze', default='hackathon.py')
	args = parser.parse_args(argv)

	try:
		report = analyze_file(args.path)
	except Exception as e:
		print(json.dumps({"error": str(e)}))
		sys.exit(1)

	print(json.dumps(report, indent=2))


if __name__ == '__main__':
	main()


