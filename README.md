
[![Test](../../actions/workflows/test.yml/badge.svg)](../../actions/workflows/test.yml)

# ApprovalTests.Python.StarterProject
Starter project for getting approvaltests up and running 

<!-- toc -->
## Contents

 * [Heading 1](#heading-1)
 * [Heading 2](#heading-2)
<!-- endToc -->

## Who is this project for?
Anyone that wants to do some new code in Python with Approvaltests.   
It works great for experimentation, katas or starting a green field project.

## What is included?
* Github actions - CI that runs your tests on Mac, Windows & Linux
* `requirements.txt` - standard place to include all pip dependiences 
* `tests` & `project` folders - to keep your production code and tests seperate
* Sample tests that pass - to get you off to a great start
* [MDSnippets intergration](https://github.com/simonCropp/MarkdownSnippets) to easily add code snippets to your markdown documentation

## Getting Starter

If you are familar with python, you can either download the zip or fork the code.
If you are having any difficulties, We suggest you watch the [getting started video]()

## Recommended Tooling?

* [Pycharm](https://www.jetbrains.com/pycharm/download/#section=mac) (both community and professional will work)
* [Python 3](https://www.python.org/downloads/)
* Diff Tools
  * Windows - [WinMerge](https://winmerge.org/?lang=en)
  * Mac - [DiffMerge](https://sourcegear.com/diffmerge/)   

## ApprovalTests Basics

Approvaltests uses methods that start with `verify` like `verify(object_under_test)`
The expected result is stored in a file like such:

<!-- snippet: SampleTests.test_with_json.approved.txt -->
<a id='snippet-SampleTests.test_with_json.approved.txt'></a>
```txt
{
    "age": 38,
    "firstName": "jayne",
    "isMale": true,
    "lastName": "cobb"
}
```
<sup><a href='/tests/SampleTests.test_with_json.approved.txt#L1-L6' title='Snippet source file'>snippet source</a> | <a href='#snippet-SampleTests.test_with_json.approved.txt' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

## To setup in pycharm
* Import project
* Go File > Settings > Tools > Python Integered Tools > Testing > Default Test Runner > Unittests
* From the command line run `pip install approvaltests`
* Open test file and click the green arrows by the tests to run




