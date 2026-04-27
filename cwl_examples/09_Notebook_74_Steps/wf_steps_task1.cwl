class: Workflow
cwlVersion: v1.2

inputs:
  greeting: string
  farewell: string

steps:
  echo:
    run: ./echo.cwl
    in:
      message: farewell
    out: [phrase]

outputs: []
