cwlVersion: v1.2
class: CommandLineTool
baseCommand: grep
inputs:
  search_term:
    type: string
    inputBinding:
      position: 1
  input_file:
    type: File
    inputBinding:
      position: 2
outputs:
  matches:
    type: stdout
stdout: grep_output.txt
