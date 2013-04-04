#!/usr/bin/python
import re
from sys import stderr
pattern_route=re.compile(r"^[ \t]*[0-9]{1,3}(\.[0-9]{1,3}){3,3}/[0-9]{1,2}[ \t]*(#.*)?")
pattern_comment=re.compile(r"[ \t]*#.*")
pattern_include=re.compile(r"^[ \t]*\$include[\t ][\t ]*[^#]*[\t ]*(#.*)?")
pattern_prefix=re.compile(r"^[\t ]*\$include[\t ][\t ]*")
ROUTE=1
COMMENT=2
INCLUDE=3
pattern_list=[(ROUTE,pattern_route),(COMMENT,pattern_comment),(INCLUDE,pattern_include)]
def match(line):
	for token,pattern in pattern_list:
		if pattern.match(line): return token
	print>>stderr, "Unrecognized line %s"%line
	return -1
def resolve(filename):
	try:
		fp = file(filename)
	except IOError:
		return
	for line in fp:
		line = line.strip()
		if line == "" : continue
		rc = match(line)
		if rc == ROUTE:
			cmt = pattern_comment.search(line)
			if cmt: end = cmt.span()[0]
			else:   end = len(line)
			print line[:end]
		elif rc == INCLUDE:
			cmt = pattern_comment.search(line)
			if cmt: end = cmt.span()[0]
			else:   end = len(line)
			cmt = pattern_prefix.search(line)
			if cmt: start = cmt.span()[1]
			else:   start = 0
			resolve(line[start:end])
resolve("/dev/stdin")


