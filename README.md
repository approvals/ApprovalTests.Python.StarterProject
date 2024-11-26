
[![Test](../../actions/workflows/test.yml/badge.svg)](../../actions/workflows/test.yml)

# ApprovalTests.Python.StarterProject
Starter project for getting approvaltests up and running 

<!-- toc -->
## Contents

  * [Who is this project for?](#who-is-this-project-for)
  * [Getting Started](#getting-started)
    * [Watch the video](#watch-the-video)
  * [What is included?](#what-is-included)
  * [Recommended Tooling?](#recommended-tooling)
  * [ApprovalTests Basics](#approvaltests-basics)
  * [Next steps](#next-steps)<!-- endToc -->

## Who is this project for?
Anyone that wants to do some new code in Python with Approvaltests.   
It works great for experimentation, katas or starting a green field project.

## Getting Started

If you are familar with python, you can either:
* download the zip (under the `code` button

or 
* Fork the code by pressing `use this template`

### Watch the video
If you are having any difficulties, We suggest you watch the [getting started video](https://www.youtube.com/watch?v=2PbA273JHYE)  
**tip:** pause the video after each step and do it so you are in sync


## What is included?
* [Github actions](https://github.com/approvals/ApprovalTests.Python.StarterProject/actions/workflows/test.yml) - CI that runs your tests on Mac, Windows & Linux  
   This is also what powers the green 'passing' badge at the top of this document
* `requirements.txt` - standard place to include all your [pip dependiences from pypi](https://pypi.org/) 
* `constraints.txt` - standard pinned versions of pip dependencies, including transitive dependencies
* `tox.ini' - A working [tox file](https://tox.wiki/en/latest/)
* `tests` & `project` folders - to keep your production code and tests seperate
* Sample tests that pass - to get you off to a great start
* [MDSnippets intergration](https://github.com/simonCropp/MarkdownSnippets) to easily add code snippets to your markdown documentation

## Recommended Tooling?

* [Pycharm](https://www.jetbrains.com/pycharm/download/#section=mac) (both community and professional will work)
* [Python 3](https://www.python.org/downloads/)
* Diff Tools
  * Windows - [WinMerge](https://winmerge.org/?lang=en)
  * Mac - [DiffMerge](https://sourcegear.com/diffmerge/)   

## ApprovalTests Basics

Approvaltests uses methods that start with `verify` like `verify(object_under_test)`
The expected result is stored in a file like such:

<!-- snippet: SampleTests.test_with_json.approved.json -->
<a id='snippet-SampleTests.test_with_json.approved.json'></a>
```json
{
    "age": 38,
    "firstName": "jayne",
    "isMale": true,
    "lastName": "cobb"
}
```
<sup><a href='/tests/SampleTests.test_with_json.approved.json#L1-L6' title='Snippet source file'>snippet source</a> | <a href='#snippet-SampleTests.test_with_json.approved.json' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

## Next steps

If you are just exploring you might want to try a sample exercise(kata). I would suggest you start with [LCD digits kata](https://codingdojo.org/kata/NumberToLCD/)



