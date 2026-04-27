# CWL Examples and Solutions for Day 1 - Module 2

These examples match the CWL topics in the training slides: a `.cwl` file describes the tool/workflow, and a `.yml` file gives the values used when running it.

The folders `02_grep ; 04_tar; 03_wc ; 05_workflow` are also the **solutions of the two Hands-On Exercises** (Exercise 1 ; Exercise 2) presented at the end of [Day1-Module2.pdf](../Day1-Module2.pdf)

## Install

```bash
python -m pip install cwltool
```

## Run the exercies (and solutions to Exercise 1 and Exercise 2):

From inside this folder:

The `01_hello_world` is not part of Exercise 1, neither Exercise 2. It is `hello world` example of CWL, which appears in the `Day1-Module2.pdf` slides. 

```bash
cd 01_hello_world
cwltool hello_world.cwl hello_world.yml
```

The `02_grep` folder is part of the solution for Exercise 1:

```bash
cd ../02_grep
cwltool grep.cwl grep.yml
```

The `04_tar` foleder is part of the solution for Exercise 1:

```bash
cd ../04_tar
cwltool tar_extract.cwl tar_extract.yml
```

The `03_wc` folder is part of the solution for Exerice 1:

**Important: To run `wc.cwl` by itself, first your need run the GREP example so that `02_grep/grep_output.txt` exists:

```bash
cd ../03_wc
cwltool wc.cwl wc.yml
```

The full Exercise 2 solution is in `05_workflow` folder: 

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

##  06 Input parameters example

This is not part of the solution for Exercise 1 nor Exercise 2. It just an additional example to illustrate for several input parameters, which corresponds to one of the examples shown in `Day1-Module2.pdf` slides.

The folder `06_input_parameters` reproduces the `inp.cwl` / `inp-job.yml` example from the slides.
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

## Additional notebook solution examples 

The following folders contain further solutions for the notebook sections 6.2, 7.3, 7.4 and 7.5 :

- 07_Notebook_62_outputBinding
- 08_Notebook_73_Inputs
- 09_Notebook_74_Steps
- 10_Notebook_74_StepsII
- 11_Notebook_75_Outputs
