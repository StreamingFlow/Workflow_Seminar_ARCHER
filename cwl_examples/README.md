# CWL Solution for Day 1 - Module 2

These examples match the CWL topics in the training slides: a `.cwl` file describes the tool/workflow, and a `.yml` file gives the values used when running it.

Basically these are the **solutions of the two Hands-On Exercises** (Exercise 1 ; Exercise 2) presented at the end of [Day1-Module2.pdf](../Day1-Module2.pdf)

## Install

```bash
python -m pip install cwltool
```

## Run the solutions

From inside this folder:

```bash
cd 01_hello_world
cwltool hello_world.cwl hello_world.yml
```

```bash
cd ../02_grep
cwltool grep.cwl grep.yml
```

```bash
cd ../04_tar
cwltool tar_extract.cwl tar_extract.yml
```

To run `wc.cwl` by itself, first run the GREP example so that `02_grep/grep_output.txt` exists:

```bash
cd ../03_wc
cwltool wc.cwl wc.yml
```

To run the complete workflow TAR → GREP → WC:

```bash
cd ../05_workflow
cwltool tar_grep_wc_workflow.cwl tar_grep_wc_workflow.yml
```

The final workflow output is `count.txt`, containing the number of matching lines.

## Folder contents

- `01_hello_world/`: wrapper around `echo`
- `02_grep/`: wrapper around `grep`
- `03_wc/`: wrapper around `wc -l`
- `04_tar/`: wrapper around `tar -xzf`
- `05_workflow/`: workflow chaining TAR, GREP, and WC
- `data/`: sample text file and compressed tar archive

## Aditionally, we have 06 Input parameters example


This is not part of the solution for Exercise 1 and Exercise 2. It just is to illustrate an example of input parameters.

This folder reproduces the `inp.cwl` / `inp-job.yml` example from the slides.
It demonstrates:

- boolean input flags (`example_flag` → `-f`)
- string inputs with a long prefix (`example_string` → `--example-string hello`)
- integer inputs joined to the prefix (`example_int` → `-i42`)
- file inputs (`example_file` → `--file=/path/to/whale.txt`)

Run it with:

```bash
cd 06_input_parameters
cwltool inp.cwl inp-job.yml
```
