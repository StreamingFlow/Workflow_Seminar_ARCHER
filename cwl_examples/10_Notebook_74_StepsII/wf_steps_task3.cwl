class: Workflow
cwlVersion: v1.2

inputs:
  greeting: string

steps:
  echo:
    run: ./echo.cwl
    in:
      message: greeting
    out: [phrase]

outputs:
  echo_out:
    type: File
    outputSource: echo/phrase
