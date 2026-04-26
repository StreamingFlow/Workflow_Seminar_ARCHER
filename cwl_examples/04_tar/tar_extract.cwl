cwlVersion: v1.2
class: CommandLineTool
baseCommand: tar
arguments:
  - "-xzf"
inputs:
  archive:
    type: File
    inputBinding:
      position: 1
  extracted_filename:
    type: string
    default: "data.txt"
outputs:
  extracted_file:
    type: File
    outputBinding:
      glob: $(inputs.extracted_filename)
