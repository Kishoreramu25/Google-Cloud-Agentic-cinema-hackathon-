from pathlib import Path
p = Path('/home/ubuntu/ai-script-analyzer/client/src/pages/Home.tsx')
s = p.read_text()
s = s.replace('setFiles((prev) => [...new Set([...prev, ...names])])', 'setFiles((prev) => Array.from(new Set([...prev, ...names])))')
p.write_text(s)
