# BDA — Big Data Analytics Coursework

A study repository for coursework, lecture notes, notebooks, and practice exercises from the M.Sc. Big Data Analytics programme.

## Subjects currently visible in this repository

| Folder | Contents |
|---|---|
| `DIP/` | Digital Image Processing notebooks, including filtering, edge detection, histogram equalization, image restoration, and segmentation |
| `algo/` | Algorithms and data-structure exercises, including sorting/searching, linked lists, graph algorithms, knapsack, and Python class notes |
| `creadit_risk_fds/` | Credit-risk coursework/notebooks and a dataset |
| `data_minning/` | Pandas, data-wrangling, visualization, and numerical/categorical data-handling assignments |
| `ml/` | Machine-learning notes and implementation notebooks |

This repository is primarily a **learning archive**, not a single deployable application. Notebooks may depend on files, packages, or paths from the original learning environment.

## Recommended navigation

- Start with the subject folder related to the topic you want to study.
- Open a notebook and read its first markdown cells for its purpose and required inputs.
- Check relative file paths before running a notebook in a different environment.
- Treat notebooks as coursework/experiments; promote selected, polished work to its own project repository when it has a clear objective, clean data handling, reproducible results, and a complete README.

## Suggested cleanup sequence

1. Keep material grouped by subject rather than moving all notebooks into one flat directory.
2. Normalize names gradually (for example, `credit_risk_fds` and `data_mining`) only after checking notebook imports and paths.
3. Remove accidental Jupyter checkpoint files from Git tracking after confirming they are not needed.
4. Add a short README to each subject folder describing the notebooks, inputs, and how to run them.
5. Keep original source datasets only when redistribution is permitted; use small documented sample data where possible.
6. Separate polished standalone projects from class notes so your portfolio remains easy to evaluate.

## Data provenance, licensing, and privacy

This repository is public. Document the original source and license for every dataset before redistributing it. The `creadit_risk_fds/credit_risk_dataset.csv` file appears consistent with Kaggle's [Credit Risk Dataset by Lao Tse](https://www.kaggle.com/datasets/laotse/credit-risk-dataset), whose dataset page labels it CC0/Public Domain. Because the original download/version was not retained with provenance metadata, verify that the committed file is the same release before relying on that license attribution. If it is not the same release, replace it with a verified copy or remove it. The diabetes-health-indicators notebook still needs its exact dataset source and license recorded before the notebook or any embedded data is reused.

- Keep a source URL and license/terms next to each dataset; for the credit-risk dataset, verify the source match and preserve the CC0 attribution/provenance note.
- Do not upload private or identifiable financial/medical records.
- If a dataset's redistribution permission is unclear, remove the raw copy from the public repository and document how readers can obtain it from the original source instead.
- Adding `.gitignore` does not remove data that has already been committed.

## Python/Jupyter basics

Create an isolated environment for a subject or project rather than relying on globally installed packages. The exact dependency set may differ by notebook; record tested versions in a subject-specific `requirements.txt` when you have verified them.

Typical commands:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the packages actually required by the notebook, then launch:

```bash
jupyter notebook
```

## Note

This README documents the current observed folder categories. The notebooks have not all been executed or tested in a clean environment as part of this documentation update.

## Author

Kunal Goyal — [GitHub profile](https://github.com/KunalGoyal0601)
