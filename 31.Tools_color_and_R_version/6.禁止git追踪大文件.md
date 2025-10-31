把下面两行写进仓库根目录 .gitignore 并提交——通杀所有 ≥1 MiB 的文件：
Copy

## 自动忽略体积 ≥1 MiB 的任何文件

- filter=sizeblock

接着给当前仓库（或全局）注册一个“clean”过滤器，让 Git 在 git add 阶段直接拒绝大文件：
bash
Copy

## 复制粘贴即可，跨平台（Linux/macOS/WSL/Git Bash）

git config filter.sizeblock.clean \
'f="$1"; s=$(wc -c <"$f" 2>/dev/null || stat -f%z "$f" 2>/dev/null); \
 if [ "$s" -gt 1048576 ]; then \
 echo >&2 "🚫 $f 大小 $s > 1 MiB，已拒绝"; exit 1; fi; cat'
git config filter.sizeblock.smudge cat
git config filter.sizeblock.required true
