cwlVersion: v1.2
class: CommandLineTool
baseCommand: wc
arguments:
  - "-l"
inputs:
  input_file:
    type: File
    inputBinding:
      position: 1
outputs:
  count_file:
    type: stdout
stdout: count.txt
