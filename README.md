# SWYNEX - Data Exploratory Data Analysis

## 📊 Project Overview

This project performs Exploratory Data Analysis (EDA) on a cleaned Netflix titles dataset.

The objective is to explore the dataset, calculate important statistics, identify trends and patterns, and present useful insights through data visualizations.

This project was completed as part of Task 2 of my Data Analysis Internship.

---

## 🎯 Objectives

The main objectives of this project are:

- Understand the structure of the Netflix dataset
- Analyze Movies and TV Shows distribution
- Identify trends in release years
- Analyze content ratings
- Explore the countries represented in the dataset
- Identify the most common genres/categories
- Analyze movie durations
- Analyze the number of seasons in TV Shows
- Identify useful patterns and insights using visualizations

---

## 📁 Dataset

The dataset used in this project is a cleaned version of the Netflix Titles dataset from Task 1.

### Dataset Details

- Total records: **6,234**
- Total columns: **12**
- Content types: Movies and TV Shows
- Release years: **1925–2020**

### Main Columns

- `show_id`
- `type`
- `title`
- `director`
- `cast`
- `country`
- `date_added`
- `release_year`
- `rating`
- `duration`
- `listed_in`
- `description`

---

## 🛠️ Tools and Technologies

- Python
- Pandas
- Matplotlib
- VS Code
- GitHub

---

## 🔍 Exploratory Data Analysis

The following analyses were performed:

### 1. Movies vs TV Shows

The dataset contains:

- Movies: **4,265 (68.42%)**
- TV Shows: **1,969 (31.58%)**

Movies represent the larger share of the dataset.

---

### 2. Release Year Analysis

The top release years were:

| Release Year | Number of Titles |
|---|---:|
| 2018 | 1,063 |
| 2017 | 959 |
| 2019 | 843 |
| 2016 | 830 |
| 2015 | 517 |

The highest number of titles in the dataset was released in **2018**.

---

### 3. Ratings Analysis

The most common ratings were:

| Rating | Number of Titles |
|---|---:|
| TV-MA | 2,027 |
| TV-14 | 1,698 |
| TV-PG | 701 |
| R | 508 |
| PG-13 | 286 |

**TV-MA** is the most frequently occurring rating in the dataset.

---

### 4. Country Analysis

The top countries represented in the dataset were:

| Country | Number of Titles |
|---|---:|
| United States | 2,609 |
| India | 838 |
| United Kingdom | 601 |
| Canada | 318 |
| France | 271 |
| Japan | 231 |
| Spain | 178 |
| South Korea | 162 |
| Germany | 151 |

The **United States** has the highest representation among the countries analyzed.

---

### 5. Genre Analysis

The most common categories in the `listed_in` column were:

| Genre / Category | Number of Titles |
|---|---:|
| International Movies | 1,927 |
| Dramas | 1,623 |
| Comedies | 1,113 |
| International TV Shows | 1,001 |
| Documentaries | 668 |
| TV Dramas | 599 |
| Action & Adventure | 597 |
| Independent Movies | 552 |
| TV Comedies | 436 |
| Thrillers | 392 |

**International Movies** is the most frequently occurring category.

---

## 🎬 Movie Duration Analysis

For Movies:

- Average duration: **99.1 minutes**
- Median duration: **98 minutes**
- Minimum duration: **3 minutes**
- Maximum duration: **312 minutes**

The average and median durations are close, showing that a typical movie in this dataset is approximately **99 minutes** long.

---

## 📺 TV Show Season Analysis

For TV Shows:

- Average seasons: **1.78**
- Median seasons: **1**
- 75% of shows have **2 or fewer seasons**
- Maximum seasons: **15**

This shows that most TV Shows in the dataset have relatively few seasons.

---

## 📈 Visualizations

The following charts were created using Matplotlib:

1. Movies vs TV Shows
2. Top 10 Release Years
3. Content Ratings
4. Top 10 Countries
5. Top 10 Genres

All charts are available in the `charts` folder.

---

## 💡 Key Insights

Based on the exploratory analysis, the following insights were identified:

1. **Movies make up 68.42% of the dataset**, while TV Shows account for 31.58%.
2. **2018 had the highest number of titles**, with 1,063 titles.
3. **TV-MA is the most common rating**, with 2,027 titles.
4. **The United States has the highest country representation**, with 2,609 titles.
5. **International Movies is the most common category**, with 1,927 titles.
6. The average movie duration is approximately **99 minutes**.
7. The median number of TV Show seasons is **1 season**.

---

## 🧹 Data Quality Findings

During the EDA process:

- Duplicate records: **0**
- Missing `date_added` values: **11**
- Other major columns were checked for missing values.
- Categorical columns were analyzed for their distributions.
- Multi-value fields such as countries and genres were split and analyzed separately.

---

## 📂 Project Structure

```text
SWYNEX-Data-Exploratory-Data-Analysis/
│
├── analysis/
│   └── eda.py
│
├── charts/
│   ├── content_type.png
│   ├── release_year.png
│   ├── ratings.png
│   ├── countries.png
│   └── genres.png
│
├── data/
│   └── netflix_titles_cleaned.csv
│
└── README.md