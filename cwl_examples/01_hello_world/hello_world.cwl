cwlVersion: v1.2
class: CommandLineTool
baseCommand: echo
inputs:
  message:
    type: string
    default: "Hello World"
    inputBinding:
      position: 1
outputs:
  output:
    type: stdout
stdout: hello.txt
