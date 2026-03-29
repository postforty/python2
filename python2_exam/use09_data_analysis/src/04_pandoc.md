## Pandoc 사용법 가이드

![pandoc](../assets/images/pandoc-cartoon.png)

Pandoc은 **하나의 마크업 형식에서 다른 형식으로 파일을 변환**하는 데 사용되는 유니버설 문서 변환 도구입니다.

### 1\. 기본 설치 및 사용법

#### 1.1. 설치

Pandoc은 다양한 운영체제(Windows, macOS, Linux)에서 설치할 수 있습니다. 각 시스템에 맞는 설치 관리자나 패키지 관리자를 사용하여 설치합니다.

#### 1.2. 기본 변환 명령어

Pandoc의 기본 사용 문법은 **`pandoc [옵션] [입력 파일] -o [출력 파일]`** 형태입니다.

- **예시 (md $\to$ html 변환):**

  ```bash
  pandoc input.md -o output.html
  ```

- **예시 (ipynb $\to$ docx 변환):**

  ```bash
  pandoc input.ipynb -o output.docx
  ```

---

### 2\. 주요 변환 옵션

Pandoc은 변환 과정에서 문서의 구조와 형식을 세밀하게 제어할 수 있는 다양한 옵션을 제공합니다.

#### 2.1. `--toc` (Table of Contents)

출력 문서에 **자동으로 목차를 생성**합니다. 목차는 문서 내의 제목(`#`, `##`, `###` 등)을 기반으로 생성됩니다.

- **예시:**
  ```bash
  pandoc input.md -o output.pdf --toc
  ```

#### 2.2. `--number-sections` (섹션 번호 매기기)

문서의 **모든 제목(섹션)에 번호를 자동**으로 매깁니다.

- **예시:**
  ```bash
  pandoc input.md -o output.html --number-sections
  ```

#### 2.3. `--standalone` 또는 `-s` (독립적인 문서 생성)

출력 파일이 **머리글, 바닥글 등**을 포함하는 완전한 독립형 문서가 되도록 지정합니다. 예를 들어, HTML 변환 시 스타일시트 등을 포함하는 완전한 HTML 파일을 생성합니다.

- **예시:**
  ```bash
  pandoc input.md -s -o output.html
  ```

---

### 3\. 다양한 형식으로 변환 예제

| 입력 형식                   | 출력 형식        | 명령어 예시                                           |
| :-------------------------- | :--------------- | :---------------------------------------------------- |
| Markdown (`.md`)            | HTML (`.html`)   | `pandoc input.md -o output.html`                      |
| Markdown (`.md`)            | PDF (`.pdf`)     | `pandoc input.md -o output.pdf` (LaTeX 설치 필요)     |
| Markdown (`.md`)            | DOCX (`.docx`)   | `pandoc input.md -o output.docx`                      |
| Markdown (`.md`)            | EPUB (`.epub`)   | `pandoc input.md -o output.epub`                      |
| Jupyter Notebook (`.ipynb`) | Markdown (`.md`) | `pandoc input.ipynb -o output.md` (Jupyter 설치 필요) |

---

### 4\. 스타일 및 템플릿 제어

#### 4.1. `--css` (HTML 스타일 지정)

HTML 파일로 변환 시 **외부 CSS 파일**을 연결하여 스타일을 지정합니다.

- **예시:**
  ```bash
  pandoc input.md -s --css custom.css -o output.html
  ```

#### 4.2. `--template` (사용자 정의 템플릿)

출력 형식을 세부적으로 제어하기 위해 **사용자 정의 템플릿** 파일을 사용합니다. 이는 특히 PDF나 HTML 출력 시 문서의 레이아웃을 표준화하는 데 유용합니다.

- **예시:**
  ```bash
  pandoc input.md -o output.pdf --template my_custom_template.latex
  ```

Pandoc은 이 외에도 수많은 옵션과 기능을 제공하며, 자세한 내용은 공식 문서를 참조하세요.

> Pandoc 공식 문서 URL: <https://pandoc.org>
