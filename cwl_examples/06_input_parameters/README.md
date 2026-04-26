# Input parameters example

This example shows different CWL input types and how `inputBinding` controls the command line.

Run from this folder:

```bash
cwltool inp.cwl inp-job.yml
```

You should see `echo` receive arguments similar to:

```bash
-f -i42 --example-string hello --file=/path/to/whale.txt
```

Note: In this example, whale.txt is an input file, not an output file. So CWL/cwltool copies or stages it into a temporary working directory, then passes that temporary path to echo:
```bash
--file=/private/tmp/docker_tmp.../whale.txt
```

So it prints the arguments. It does not create or return a file.

You would only see an output file in your directory if the CWL tool had something like:

```
stdout: output.txt

outputs:
  output:
    type: stdout

```
