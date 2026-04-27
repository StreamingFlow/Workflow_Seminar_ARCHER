#!/usr/bin/env cwl-runner
cwlVersion: v1.2
class: CommandLineTool

baseCommand: [tar, --extract]

inputs:
  tarfile:
    type: File
    inputBinding:
      prefix: --file

outputs:
  out1:
    type: File
    outputBinding:
      glob: goodbye.txt

  out2:
    type: File
    outputBinding:
      glob: hello.txt
