cwlVersion: v1.2
class: Workflow
inputs:
  archive: File
  extracted_filename: string
  search_term: string
outputs:
  final_count:
    type: File
    outputSource: count/count_file
steps:
  extract:
    run: ../04_tar/tar_extract.cwl
    in:
      archive: archive
      extracted_filename: extracted_filename
    out: [extracted_file]
  grep:
    run: ../02_grep/grep.cwl
    in:
      search_term: search_term
      input_file: extract/extracted_file
    out: [matches]
  count:
    run: ../03_wc/wc.cwl
    in:
      input_file: grep/matches
    out: [count_file]
