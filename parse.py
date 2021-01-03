import os

words = {

}
for filename in os.listdir("."):
    if not os.path.isfile(filename):
        continue
    if not "Words" in filename and \
            not "Reserved" in filename and \
            not "words" in filename:
        print(filename)
        continue
    language = filename.split(" ")[0].lower()
    if language == "adobe":
        language = "coldfusion"
    if language == "shell":
        language = "bash"
    if language in ["force.com", "apache", "cloudera", "teradata", "vhdl",
                    "angelscript", "dynamodb"]:
        continue
    words[language] = set()
    if filename.endswith(".md"):
        with open(filename) as file:
            text = file.read()

            lines = text.split("\n")
            for line in lines:

                if (line.startswith("  - ") or line.startswith(
                        "-")) and not line.startswith("#"):
                    candidate = line.split("-")[1].strip().split(" ")[0]
                    if len(candidate) > 1 and candidate.isalpha():
                        words[language].add(candidate.lower())
keys_to_remove = []
for key, value in words.items():
    if not value:
        keys_to_remove.append(key)
for key in keys_to_remove:
    del words[key]

print(words)
final = {
    'coldfusion': {'of', 'table', 'commit', 'date', 'outer', 'order', 'connect', 'max',
                   'month', 'indicator', 'work', 'using', 'by', 'trailing', 'from',
                   'convert', 'set', 'position', 'prior', 'continue', 'rollback',
                   'deallocate', 'as', 'only', 'except', 'natural', 'corresponding',
                   'goto', 'size', 'update', 'timestamp', 'prepare', 'insert',
                   'substring', 'false', 'column', 'avg', 'real', 'usage', 'at',
                   'nchar', 'national', 'leading', 'insensitive', 'names', 'value',
                   'sql', 'language', 'execute', 'external', 'is', 'drop', 'add',
                   'privileges', 'cast', 'space', 'public', 'char', 'authorization',
                   'asc', 'min', 'assertion', 'module', 'next', 'double', 'int', 'when',
                   'character', 'fetch', 'constraints', 'trim', 'cross', 'identity',
                   'exists', 'level', 'deferred', 'pad', 'hour', 'scroll', 'no',
                   'precision', 'interval', 'last', 'begin', 'with', 'absolute', 'both',
                   'case', 'desc', 'unknown', 'on', 'session', 'count', 'found',
                   'match', 'sqlcode', 'transaction', 'escape', 'get', 'key', 'all',
                   'first', 'output', 'cascade', 'for', 'exception', 'initially',
                   'true', 'select', 'year', 'connection', 'day', 'to', 'are', 'lower',
                   'temporary', 'references', 'write', 'disconnect', 'time', 'section',
                   'translation', 'grant', 'catalog', 'collate', 'foreign', 'read',
                   'overlaps', 'descriptor', 'second', 'bit', 'varchar', 'global',
                   'constraint', 'between', 'or', 'restrict', 'schema', 'coalesce',
                   'action', 'describe', 'float', 'option', 'create', 'immediate',
                   'union', 'sqlerror', 'collation', 'declare', 'integer', 'zone',
                   'isolation', 'nullif', 'end', 'decimal', 'upper', 'values',
                   'varying', 'null', 'preserve', 'join', 'primary', 'whenever',
                   'where', 'cursor', 'intersect', 'smallint', 'and', 'having', 'in',
                   'deferrable', 'any', 'not', 'close', 'dec', 'go', 'group',
                   'procedure', 'domain', 'diagnostics', 'distinct', 'rows', 'user',
                   'local', 'left', 'right', 'partial', 'relative', 'delete', 'into',
                   'unique', 'check', 'exec', 'current', 'extract', 'numeric', 'sum',
                   'then', 'minute', 'inner', 'input', 'allocate', 'alter', 'open',
                   'full', 'sqlstate', 'translate', 'like', 'else', 'default', 'view',
                   'revoke', 'some', 'cascaded'},
    'c': {'while', 'for', 'signed', 'short', 'long', 'struct', 'char', 'break', 'const',
          'static', 'register', 'double', 'extern', 'continue', 'int', 'if', 'entry',
          'return', 'switch', 'goto', 'do', 'void', 'float', 'typedef', 'enum',
          'sizeof', 'union', 'else', 'default', 'case', 'unsigned', 'auto', 'volatile'},
    'c#': {'interface', 'internal', 'unchecked', 'using', 'throw', 'operator', 'from',
           'sbyte', 'short', 'set', 'const', 'static', 'continue', 'orderby', 'as',
           'namespace', 'ascending', 'let', 'goto', 'protected', 'finally', 'params',
           'enum', 'false', 'unsafe', 'virtual', 'out', 'value', 'is', 'add', 'public',
           'break', 'char', 'double', 'int', 'delegate', 'string', 'sealed', 'override',
           'ref', 'new', 'do', 'void', 'fixed', 'sizeof', 'dynamic', 'byte', 'case',
           'private', 'get', 'while', 'descending', 'for', 'true', 'try', 'select',
           'bool', 'remove', 'switch', 'abstract', 'event', 'global', 'foreach',
           'float', 'var', 'uint', 'implicit', 'ulong', 'explicit', 'decimal',
           'volatile', 'object', 'null', 'lock', 'join', 'yield', 'where', 'catch',
           'async', 'checked', 'class', 'in', 'long', 'typeof', 'struct', 'stackalloc',
           'extern', 'group', 'if', 'partial', 'return', 'into', 'alias', 'this',
           'readonly', 'else', 'default', 'base', 'ushort', 'await'},
    'c++': {'asm', 'typeid', 'friend', 'inline', 'null', 'while', 'using', 'npos',
            'throw', 'for', 'catch', 'mutable', 'operator', 'true', 'try', 'include',
            'iostream', 'short', 'class', 'explicit', 'public', 'and', 'long',
            'iomanip', 'struct', 'char', 'break', 'cout', 'static', 'not', 'register',
            'double', 'extern', 'bool', 'continue', 'std', 'int', 'template', 'if',
            'endl', 'namespace', 'xor', 'bitor', 'string', 'entry', 'return', 'switch',
            'goto', 'delete', 'protected', 'new', 'do', 'bitand', 'compl', 'this',
            'void', 'typename', 'or', 'float', 'typedef', 'sizeof', 'union', 'false',
            'cin', 'else', 'default', 'case', 'unsigned', 'main', 'private', 'auto',
            'volatile', 'virtual'},
    'go': {'func', 'interface', 'for', 'select', 'type', 'struct', 'break', 'defer',
           'const', 'chan', 'continue', 'go', 'package', 'import', 'if', 'return',
           'switch', 'goto', 'range', 'map', 'fallthrough', 'var', 'else', 'default',
           'case'},
    'haskell': {'newtype', 'mdo', 'where', 'data', 'class', 'instance', 'type',
                'module', 'import', 'as', 'foreign', 'qualified', 'proc', 'rec',
                'deriving', 'hiding', 'do', 'forall', 'default'},
    'java': {'assert', 'boolean', 'null', 'super', 'interface', 'while', 'throw', 'for',
             'catch', 'try', 'true', 'extends', 'class', 'short', 'public',
             'instanceof', 'long', 'break', 'char', 'transient', 'imports', 'const',
             'static', 'double', 'continue', 'int', 'package', 'strictfp',
             'synchronized', 'if', 'final', 'return', 'switch', 'abstract', 'goto',
             'protected', 'finally', 'do', 'new', 'this', 'void', 'float', 'native',
             'enum', 'implement', 'false', 'else', 'default', 'byte', 'throws', 'case',
             'private', 'volatile'},
    'javascript': {'boolean', 'date', 'super', 'infinity', 'prototype', 'javapackage',
                   'navigator', 'export', 'status', 'throw', 'fileupload', 'hidden',
                   'forms', 'top', 'screeny', 'frames', 'implements', 'onmouseup',
                   'layer', 'transient', 'static', 'mimetypes', 'function', 'elements',
                   'embeds', 'onfocus', 'anchors', 'final', 'goto', 'finally', 'submit',
                   'onclick', 'enum', 'length', 'alert', 'layers', 'radio',
                   'innerheight', 'onmouseover', 'decodeuricomponent', 'document',
                   'onmousedown', 'encodeuricomponent', 'window', 'defaultstatus',
                   'onerror', 'self', 'settimeout', 'public', 'array', 'button',
                   'closed', 'char', 'offscreenbuffering', 'undefined', 'onkeypress',
                   'int', 'unescape', 'encodeuri', 'synchronized', 'valueof', 'string',
                   'plugin', 'frame', 'new', 'do', 'decodeuri', 'scroll', 'number',
                   'getclass', 'image', 'pageyoffset', 'with', 'byte', 'throws',
                   'crypto', 'link', 'assign', 'javaclass', 'escape', 'taint', 'math',
                   'all', 'true', 'setinterval', 'onsubmit', 'select', 'javaarray',
                   'confirm', 'instanceof', 'packages', 'eval', 'navigate', 'location',
                   'history', 'untaint', 'propertyisenum', 'javaobject', 'form', 'blur',
                   'abstract', 'event', 'constructor', 'clearinterval', 'option',
                   'textarea', 'var', 'embed', 'clientinformation', 'pagexoffset',
                   'parseint', 'arguments', 'volatile', 'framerate', 'name', 'object',
                   'onkeyup', 'debugger', 'isfinite', 'yield', 'anchor', 'outerwidth',
                   'secure', 'catch', 'parsefloat', 'outerheight', 'onblur', 'class',
                   'cleartimeout', 'text', 'images', 'onkeydown', 'focus', 'close',
                   'area', 'java', 'if', 'nan', 'return', 'isnan', 'element',
                   'isprototypeof', 'checkbox', 'tostring', 'innerwidth', 'screenx',
                   'password', 'prompt', 'native', 'open', 'hasownproperty', 'parent',
                   'else', 'default', 'onload', 'opener', 'reset'},
    'mariadb': {'table', 'outer', 'order', 'iterate', 'databases', 'call', 'dual',
                'using', 'show', 'by', 'trailing', 'from', 'convert', 'accessible',
                'tinyblob', 'index', 'change', 'set', 'tinytext', 'continue', 'replace',
                'as', 'xor', 'require', 'natural', 'bigint', 'undo', 'range', 'limit',
                'update', 'mediumint', 'reads', 'separator', 'tinyint', 'keys',
                'insert', 'false', 'real', 'usage', 'asensitive', 'leading', 'out',
                'insensitive', 'optionally', 'general', 'escaped', 'resignal', 'sql',
                'force', 'is', 'drop', 'add', 'purge', 'zerofill', 'mediumtext', 'char',
                'asc', 'rlike', 'double', 'middleint', 'unlock', 'int', 'when',
                'character', 'fetch', 'schemas', 'cross', 'spatial', 'use', 'each',
                'exists', 'inout', 'varbinary', 'longblob', 'optimize', 'precision',
                'interval', 'elseif', 'ssl', 'with', 'localtime', 'both', 'case',
                'desc', 'on', 'regexp', 'match', 'varcharacter', 'key', 'while', 'all',
                'kill', 'slow', 'cascade', 'for', 'true', 'select', 'enclosed', 'to',
                'localtimestamp', 'references', 'write', 'linear', 'before', 'longtext',
                'condition', 'grant', 'analyze', 'distinctrow', 'foreign', 'collate',
                'modifies', 'binary', 'outfile', 'maxvalue', 'read', 'exit',
                'terminated', 'deterministic', 'varchar', 'div', 'constraint',
                'explain', 'between', 'or', 'restrict', 'schema', 'float', 'describe',
                'option', 'create', 'trigger', 'union', 'unsigned', 'declare',
                'integer', 'fulltext', 'delayed', 'decimal', 'values', 'varying',
                'null', 'lock', 'rename', 'sqlexception', 'primary', 'join', 'where',
                'cursor', 'lines', 'starting', 'repeat', 'mediumblob', 'load',
                'smallint', 'and', 'having', 'in', 'long', 'signal', 'not', 'partition',
                'dec', 'infile', 'procedure', 'group', 'distinct', 'if', 'leave',
                'left', 'right', 'blob', 'return', 'delete', 'into', 'sensitive',
                'unique', 'check', 'ignore', 'numeric', 'then', 'loop', 'inner', 'mod',
                'database', 'specific', 'alter', 'sqlstate', 'like', 'else', 'default',
                'revoke', 'release', 'sqlwarning', 'column'},
    'objective-c': {'out', 'null', 'inline', 'nil', 'super', 'yes', 'while', 'byref',
                    'oneway', 'for', 'self', 'nonatomic', 'bycopy', 'signed', 'short',
                    'class', 'in', 'long', 'struct', 'char', 'break', 'const', 'static',
                    'register', 'double', 'extern', 'bool', 'continue', 'int', 'sel',
                    'if', 'imp', 'id', 'atomic', 'return', 'switch', 'goto', 'do',
                    'inout', 'restrict', 'void', 'no', 'float', 'typedef', 'enum',
                    'protocol', 'retain', 'sizeof', 'union', 'else', 'default', 'case',
                    'unsigned', 'auto', 'volatile'},
    'oracle': {'of', 'comment', 'table', 'date', 'order', 'connect', 'successful', 'by',
               'from', 'index', 'set', 'raw', 'prior', 'as', 'modify', 'size', 'online',
               'update', 'insert', 'nowait', 'column', 'file', 'cluster', 'row', 'is',
               'drop', 'add', 'privileges', 'public', 'char', 'asc', 'uid', 'synonym',
               'nocompress', 'exists', 'level', 'validate', 'number', 'noaudit', 'with',
               'desc', 'on', 'session', 'access', 'identified', 'all', 'increment',
               'for', 'select', 'to', 'minus', 'grant', 'sysdate', 'varchar', 'or',
               'float', 'option', 'create', 'initial', 'trigger', 'share', 'immediate',
               'union', 'rownum', 'start', 'audit', 'integer', 'decimal', 'values',
               'null', 'lock', 'rename', 'mode', 'whenever', 'where', 'compress',
               'exclusive', 'maxextents', 'offline', 'intersect', 'smallint', 'and',
               'having', 'in', 'long', 'resource', 'any', 'not', 'group', 'rows',
               'distinct', 'user', 'delete', 'into', 'unique', 'check', 'current',
               'mlslabel', 'then', 'pctfree', 'alter', 'like', 'else', 'default',
               'view', 'revoke', 'rowid', 'between'},
    'php': {'yield', 'interface', 'while', 'endswitch', 'throw', 'endif', 'catch',
            'for', 'trait', 'include', 'try', 'extends', 'class', 'and', 'public',
            'instanceof', 'implements', 'break', 'const', 'static', 'endwhile',
            'continue', 'function', 'if', 'print', 'as', 'namespace', 'xor', 'require',
            'final', 'echo', 'return', 'switch', 'abstract', 'goto', 'protected',
            'finally', 'do', 'new', 'use', 'global', 'insteadof', 'enddeclare',
            'callable', 'foreach', 'or', 'endfor', 'elseif', 'var', 'else', 'clone',
            'default', 'case', 'endforeach', 'declare', 'private'},
    'postgresql': {'unnamed', 'commit', 'backward', 'call', 'indicator', 'work',
                   'index', 'listen', 'prefix', 'continue', 'function', 'version',
                   'unnest', 'stdout', 'cycle', 'reads', 'options', 'length', 'false',
                   'cascaded', 'avg', 'infix', 'overlay', 'cube', 'row', 'force', 'add',
                   'chain', 'module', 'transform', 'template', 'style', 'granted',
                   'security', 'inout', 'isnull', 'pad', 'statistics', 'scroll',
                   'recursive', 'begin', 'with', 'dynamic', 'both', 'access', 'sqlcode',
                   'serializable', 'key', 'exception', 'free', 'state', 'select', 'day',
                   'temporary', 'destructor', 'instead', 'encoding', 'ilike',
                   'translation', 'treat', 'overlaps', 'postfix', 'varchar',
                   'constructor', 'global', 'explain', 'schema', 'float', 'share',
                   'union', 'start', 'integer', 'nullif', 'role', 'varying', 'mode',
                   'whenever', 'join', 'checked', 'createuser', 'ordinality',
                   'intersect', 'in', 'fortran', 'grouping', 'verbose', 'offset',
                   'referencing', 'left', 'setof', 'blob', 'extract', 'numeric', 'then',
                   'system', 'alter', 'method', 'translate', 'abort', 'savepoint',
                   'valid', 'some', 'existing', 'boolean', 'date', 'outer',
                   'repeatable', 'using', 'trailing', 'from', 'unencrypted', 'vacuum',
                   'convert', 'nocreatedb', 'set', 'position', 'except', 'bigint',
                   'size', 'implementation', 'initialize', 'assignment', 'asensitive',
                   'national', 'leading', 'value', 'general', 'sql', 'execute',
                   'external', 'is', 'space', 'authorization', 'asc', 'min', 'scale',
                   'when', 'fetch', 'each', 'level', 'transforms', 'hour', 'number',
                   'last', 'committed', 'desc', 'validator', 'pascal', 'found',
                   'transaction', 'preorder', 'cascade', 'initially', 'until', 'less',
                   'are', 'bitvar', 'localtimestamp', 'references', 'write', 'simple',
                   'owner', 'section', 'catalog', 'collate', 'contains', 'binary',
                   'read', 'maxvalue', 'large', 'bit', 'truncate', 'constraint',
                   'option', 'trigger', 'immediate', 'implicit', 'collation',
                   'dictionary', 'object', 'after', 'sqlexception', 'preserve',
                   'primary', 'exclusive', 'smallint', 'and', 'statement', 'any',
                   'recheck', 'not', 'group', 'rows', 'diagnostics', 'distinct', 'user',
                   'right', 'relative', 'unique', 'check', 'password', 'handler',
                   'inner', 'copy', 'mod', 'allocate', 'open', 'full', 'view', 'admin',
                   'encrypted', 'sqlwarning', 'reset', 'source', 'freeze', 'of', 'than',
                   'completion', 'path', 'iterate', 'show', 'by', 'nullable', 'nothing',
                   'prior', 'static', 'rollback', 'routine', 'replace', 'as', 'notnull',
                   'modify', 'only', 'final', 'natural', 'rule', 'corresponding',
                   'goto', 'update', 'timestamp', 'substring', 'real', 'usage', 'nchar',
                   'characteristics', 'depth', 'cluster', 'language', 'trusted', 'drop',
                   'more', 'privileges', 'cast', 'public', 'array', 'assertion',
                   'double', 'int', 'procedural', 'similar', 'character', 'dispatch',
                   'constraints', 'oids', 'clob', 'sysid', 'trim', 'off', 'cross',
                   'identity', 'ref', 'returns', 'new', 'destroy', 'precision', 'cobol',
                   'absolute', 'localtime', 'structure', 'unknown', 'on', 'toast',
                   'session', 'storage', 'get', 'sublist', 'increment', 'asymmetric',
                   'first', 'search', 'notify', 'true', 'deref', 'connection', 'to',
                   'immutable', 'temp', 'disconnect', 'before', 'pendant', 'analyze',
                   'specifictype', 'terminate', 'createdb', 'descriptor',
                   'deterministic', 'sets', 'restrict', 'variable', 'create',
                   'sqlerror', 'symmetric', 'declare', 'reindex', 'end', 'upper',
                   'values', 'volatile', 'rename', 'where', 'having', 'nocreateuser',
                   'none', 'deferrable', 'delimiter', 'procedure', 'stable', 'delete',
                   'into', 'sensitive', 'breadth', 'exec', 'current', 'ignore', 'alias',
                   'map', 'minute', 'equals', 'database', 'specific', 'sqlstate',
                   'nclob', 'unlisten', 'default', 'revoke', 'between', 'comment',
                   'table', 'order', 'connect', 'max', 'month', 'strict', 'mumps',
                   'operator', 'called', 'ada', 'type', 'generated', 'deallocate',
                   'atomic', 'defined', 'limit', 'cache', 'forward', 'prepare',
                   'insert', 'result', 'at', 'lancompiler', 'out', 'insensitive',
                   'names', 'locator', 'self', 'abs', 'cardinality', 'char', 'next',
                   'checkpoint', 'host', 'sequence', 'hierarchy', 'exists', 'do',
                   'deferred', 'pli', 'no', 'operation', 'interval', 'overriding',
                   'uncommitted', 'case', 'definer', 'instantiable', 'count', 'match',
                   'escape', 'invoker', 'all', 'output', 'data', 'parameter', 'for',
                   'year', 'instance', 'lower', 'move', 'analyse', 'location',
                   'inherits', 'under', 'rollup', 'time', 'grant', 'parameters',
                   'foreign', 'modifies', 'every', 'second', 'aggregate', 'or',
                   'coalesce', 'action', 'describe', 'conversion', 'zone', 'isolation',
                   'decimal', 'name', 'null', 'lock', 'minvalue', 'cursor',
                   'delimiters', 'load', 'without', 'class', 'old', 'close', 'dec',
                   'go', 'domain', 'local', 'scope', 'partial', 'hold', 'return',
                   'stdin', 'sum', 'placing', 'input', 'like', 'else', 'lateral',
                   'column'},
    'python': {'assert', 'while', 'def', 'cos', 'raise', 'data', 'for', 'is', 'try',
               'from', 'del', 'class', 'and', 'in', 'type', 'pass', 'array', 'break',
               'log', 'not', 'close', 'write', 'continue', 'int', 'acos', 'import',
               'if', 'print', 'exp', 'floor', 'elif', 'tan', 'except', 'lambda',
               'oxphys', 'return', 'finally', 'range', 'exec', 'global', 'numeric',
               'or', 'fabs', 'input', 'float', 'atan', 'asin', 'open', 'zeros', 'pi',
               'sqrt', 'else', 'sin'},
    'ruby': {'nil', 'super', 'yield', 'unless', 'while', 'def', 'for', 'self', 'ensure',
             'elsif', 'true', 'until', 'retry', 'class', 'and', 'in', 'undef', 'break',
             'next', 'module', 'not', 'when', 'if', 'rescue', 'redo', 'return', 'do',
             'alias', 'then', 'or', 'begin', 'false', 'else', 'case', 'end'},
    'sql': {'of', 'boolean', 'table', 'commit', 'outer', 'order', 'xml', 'connect',
            'max', 'call', 'indicator', 'work', 'using', 'by', 'ltrim', 'trailing',
            'from', 'convert', 'set', 'prior', 'continue', 'function', 'rollback',
            'deallocate', 'as', 'only', 'except', 'natural', 'corresponding', 'goto',
            'update', 'prepare', 'insert', 'substring', 'false', 'column', 'avg',
            'real', 'at', 'nchar', 'national', 'out', 'insensitive', 'endexec', 'sql',
            'execute', 'external', 'is', 'drop', 'add', 'privileges', 'cast', 'space',
            'public', 'char', 'authorization', 'asc', 'min', 'assertion', 'next',
            'double', 'int', 'character', 'fetch', 'constraints', 'nvarchar',
            'identity', 'exists', 'inout', 'deferred', 'pad', 'hour', 'scroll', 'no',
            'last', 'begin', 'with', 'both', 'case', 'desc', 'unknown', 'on', 'count',
            'found', 'match', 'sqlcode', 'transaction', 'escape', 'get', 'key', 'all',
            'first', 'output', 'xmlparse', 'cascade', 'for', 'exception', 'initially',
            'true', 'select', 'year', 'connection', 'to', 'are', 'lower', 'temporary',
            'references', 'write', 'disconnect', 'substr', 'translation', 'grant',
            'foreign', 'collate', 'read', 'overlaps', 'second', 'bit', 'varchar',
            'global', 'constraint', 'explain', 'between', 'or', 'restrict', 'schema',
            'float', 'describe', 'option', 'create', 'immediate', 'union', 'sqlerror',
            'collation', 'declare', 'integer', 'rtrim', 'isolation', 'nullif', 'end',
            'decimal', 'upper', 'values', 'varying', 'null', 'preserve', 'join',
            'primary', 'whenever', 'where', 'cursor', 'intersect', 'smallint', 'and',
            'having', 'in', 'deferrable', 'any', 'not', 'close', 'dec', 'go', 'group',
            'procedure', 'longint', 'diagnostics', 'distinct', 'rows', 'user',
            'xmlexists', 'left', 'right', 'partial', 'relative', 'delete', 'into',
            'unique', 'check', 'exec', 'current', 'sum', 'numeric', 'xmlserialize',
            'minute', 'inner', 'input', 'allocate', 'alter', 'open', 'full', 'sqlstate',
            'translate', 'like', 'else', 'view', 'revoke', 'some', 'cascaded'},
    'sqlite': {'of', 'table', 'commit', 'outer', 'order', 'autoincrement', 'using',
               'by', 'from', 'vacuum', 'index', 'set', 'query', 'rollback', 'replace',
               'as', 'notnull', 'except', 'natural', 'fail', 'limit', 'update',
               'insert', 'attach', 'plan', 'detach', 'virtual', 'row', 'raise', 'is',
               'drop', 'add', 'cast', 'asc', 'glob', 'when', 'cross', 'each', 'exists',
               'isnull', 'deferred', 'recursive', 'no', 'begin', 'with', 'indexed',
               'desc', 'case', 'on', 'regexp', 'transaction', 'match', 'escape', 'key',
               'all', 'cascade', 'for', 'initially', 'select', 'to', 'temporary',
               'instead', 'references', 'temp', 'before', 'analyze', 'foreign',
               'collate', 'constraint', 'explain', 'between', 'or', 'restrict',
               'action', 'create', 'trigger', 'immediate', 'union', 'reindex', 'end',
               'values', 'after', 'null', 'pragma', 'rename', 'primary', 'join',
               'where', 'exclusive', 'intersect', 'without', 'and', 'having', 'in',
               'deferrable', 'not', 'group', 'distinct', 'if', 'offset', 'left',
               'right', 'conflict', 'delete', 'into', 'unique', 'check', 'ignore',
               'then', 'inner', 'database', 'alter', 'full', 'abort', 'like', 'else',
               'default', 'savepoint', 'view', 'release', 'column'},
    'transact-sql': {'commit', 'call', 'indicator', 'work', 'xmliterate', 'offsets',
                     'distributed', 'backup', 'index', 'prefix', 'continue', 'function',
                     'unnest', 'disk', 'cycle', 'xmlattributes', 'reads', 'false',
                     'column', 'avg', 'xmlbinary', 'unpivot', 'overlay', 'window',
                     'cube', 'row', 'fulltexttable', 'include', 'add', 'sqlca', 'break',
                     'module', 'xmltext', 'fusion', 'use', 'xmlconcat', 'pad', 'inout',
                     'statistics', 'scroll', 'recursive', 'ln', 'begin', 'with',
                     'clustered', 'dynamic', 'both', 'sqlcode', 'key', 'exception',
                     'free', 'state', 'select', 'day', 'tablesample', 'temporary',
                     'destructor', 'translation', 'intersection', 'xmlelement',
                     'xmltable', 'treat', 'overlaps', 'postfix', 'varchar',
                     'constructor', 'global', 'schema', 'float', 'xmlagg', 'union',
                     'start', 'integer', 'nullif', 'role', 'varying', 'whenever',
                     'join', 'xmldocument', 'ordinality', 'intersect', 'in', 'fortran',
                     'grouping', 'if', 'referencing', 'left', 'blob', 'waitfor',
                     'extract', 'numeric', 'then', 'xmlserialize', 'system', 'alter',
                     'method', 'translate', 'collect', 'savepoint', 'release', 'some',
                     'boolean', 'outer', 'date', 'using', 'trailing', 'from', 'convert',
                     'revert', 'openxml', 'set', 'position', 'shutdown', 'openquery',
                     'except', 'size', 'initialize', 'xmlcomment', 'tsequal',
                     'asensitive', 'national', 'file', 'leading', 'value', 'compute',
                     'readtext', 'general', 'freetexttable', 'sql', 'execute',
                     'external', 'is', 'space', 'authorization', 'asc', 'bulk', 'min',
                     'when', 'fetch', 'dbcc', 'each', 'level', 'hour', 'tran', 'last',
                     'save', 'desc', 'xmlnamespaces', 'pascal', 'transaction', 'found',
                     'preorder', 'kill', 'cascade', 'initially', 'less', 'are',
                     'localtimestamp', 'references', 'write', 'section', 'fillfactor',
                     'read', 'collate', 'contains', 'catalog', 'binary', 'large',
                     'securityaudit', 'truncate', 'bit', 'constraint', 'multiset',
                     'textsize', 'option', 'trigger', 'immediate', 'percent',
                     'collation', 'dictionary', 'object', 'after', 'xmlcast',
                     'sqlexception', 'filter', 'primary', 'preserve', 'smallint', 'and',
                     'statement', 'any', 'not', 'group', 'rows', 'distinct',
                     'diagnostics', 'user', 'right', 'restore', 'relative', 'unique',
                     'check', 'inner', 'mod', 'allocate', 'open', 'full', 'view',
                     'admin', 'sqlwarning', 'of', 'than', 'completion', 'path',
                     'iterate', 'deny', 'by', 'setuser', 'prior', 'static', 'holdlock',
                     'rollback', 'routine', 'as', 'only', 'modify', 'natural', 'rule',
                     'corresponding', 'goto', 'corr', 'update', 'timestamp',
                     'substring', 'real', 'plan', 'usage', 'nchar', 'depth', 'language',
                     'drop', 'privileges', 'cast', 'nonclustered', 'public', 'array',
                     'writetext', 'assertion', 'double', 'int', 'similar', 'character',
                     'constraints', 'trim', 'clob', 'off', 'cross', 'identity', 'ref',
                     'returns', 'xmlquery', 'new', 'destroy', 'precision', 'absolute',
                     'localtime', 'normalize', 'xmlforest', 'structure', 'nocheck',
                     'within', 'on', 'unknown', 'session', 'get', 'xmlparse', 'first',
                     'asymmetric', 'search', 'true', 'deref', 'connection', 'to',
                     'disconnect', 'before', 'condition', 'specifictype', 'terminate',
                     'descriptor', 'deterministic', 'semanticsimilaritydetailstable',
                     'sets', 'errlvl', 'restrict', 'variable', 'create', 'raiserror',
                     'sqlerror', 'replication', 'symmetric', 'declare', 'end', 'values',
                     'upper', 'rowcount', 'freetext', 'where', 'having', 'none',
                     'deferrable', 'partition', 'procedure', 'xmlvalidate', 'browse',
                     'delete', 'into', 'sensitive', 'breadth', 'exec', 'current',
                     'reconfigure', 'over', 'alias', 'ignore', 'map', 'minute',
                     'equals', 'database', 'specific', 'member', 'sqlstate', 'nclob',
                     'default', 'containstable', 'revoke', 'between', 'table', 'order',
                     'connect', 'max', 'month', 'called', 'ada', 'top', 'deallocate',
                     'atomic', 'semantickeyphrasetable', 'range', 'limit', 'prepare',
                     'insert', 'result', 'opendatasource', 'lineno', 'at', 'out',
                     'insensitive', 'names', 'uescape', 'locator', 'cardinality',
                     'char', 'next', 'checkpoint', 'host', 'print', 'sequence', 'proc',
                     'exists', 'deferred', 'no', 'operation', 'interval', 'case',
                     'pivot', 'count', 'match', 'escape', 'while', 'all', 'output',
                     'data', 'rowguidcol', 'for', 'parameter', 'year', 'identitycol',
                     'semanticsimilaritytable', 'lower', 'under', 'time', 'rollup',
                     'grant', 'dump', 'foreign', 'modifies', 'parameters', 'every',
                     'exit', 'second', 'submultiset', 'aggregate', 'or', 'coalesce',
                     'action', 'describe', 'openrowset', 'xmlpi', 'zone', 'isolation',
                     'decimal', 'null', 'cursor', 'load', 'without', 'class', 'old',
                     'close', 'dec', 'go', 'domain', 'local', 'scope', 'xmlexists',
                     'partial', 'merge', 'return', 'element', 'hold', 'updatetext',
                     'sum', 'input', 'like', 'else', 'lateral', 'cascaded'}}
