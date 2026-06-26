---
title: Page Template
url: page-template/
save_as: page-template/index.html
slug: page-template
tags: Template, Meta
date: 2018-08-18
modified: 2018-11-10
---

Now we’re creating the markdown files. Prepending them with a number ensures that they appear in the order you specify.

Text can be **bold**, _italic_, or ~~strikethrough~~.

### Internal Pelican Links
Link to another note using the filename to ensure the URL never breaks:
[My Essay on Consciousness]({filename}/_pages/philosophy/consciousness.md)

Link to an image reliably using the static tag:
![My Diagram]({static}/images/Raphael_School_of_Athens.jpg)

# Kramdown
[Link to another page](./another-page.html).

There should be whitespace between paragraphs.

There should be whitespace between paragraphs. We recommend including a README, or a file with information about your project.

# Header 1

This is a normal paragraph following a header. GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.

## Header 2

> This is a blockquote following a header.
>
> When something is important enough, you do it even if the odds are not in your favor.

### Header 3

```python
# Python code with syntax highlighting
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/api/progress')
def get_progress():
    """Retrieve skill tracking data for the dashboard."""
    user_stats = {"jiu_jitsu_hours": 12, "python_level": "advanced"}
    return user_stats
```

```js
// Javascript code with syntax highlighting.
var fun = function lang(l) {
  dateformat.i18n = require('./lang/' + l)
  return true;
}
```

```ruby
# Ruby code with syntax highlighting
GitHubPages::Dependencies.gems.each do |gem, version|
  s.add_dependency(gem, "= #{version}")
end
```

#### Header 4

*   This is an unordered list following a header.
*   This is an unordered list following a header.
*   This is an unordered list following a header.

##### Header 5

1.  This is an ordered list following a header.
2.  This is an ordered list following a header.
3.  This is an ordered list following a header.

###### Header 6

| head1        | head two          | three |
|:-------------|:------------------|:------|
| ok           | good swedish fish | nice  |
| out of stock | good and plenty   | nice  |
| ok           | good `oreos`      | hmm   |
| ok           | good `zoute` drop | yumm  |

### There's a horizontal rule below this.

* * *

### Here is an unordered list:

*   Item foo
*   Item bar
*   Item baz
*   Item zip

### And an ordered list:

1.  Item one
1.  Item two
1.  Item three
1.  Item four

### And a nested list:

- level 1 item
  - level 2 item
  - level 2 item
    - level 3 item
    - level 3 item
- level 1 item
  - level 2 item
  - level 2 item
  - level 2 item
- level 1 item
  - level 2 item
  - level 2 item
- level 1 item

### Task Lists
- [x] Complete the Flask backend integration
- [ ] Train 5 hours of Jiu-Jitsu this week
- [ ] Review literature on AGI benchmarking

### Footnotes
Here is a controversial statement about the nature of consciousness.[^1]

[^1]: And here is the detailed citation or tangent explaining why that statement was made, placed safely at the bottom of the document.

### Pelican Inline Image Styling
![School]({static}/images/Raphael_School_of_Athens.jpg){: style="width: 50%; border-radius: 10px;"}

### Responsive Video Embed
<div class="video-container">
    <iframe src="https://youtube.com/embed/YOUR_VIDEO_ID" frameborder="0" allowfullscreen></iframe>
</div>

### Kramdown: Small image

![Octocat](https://assets-cdn.github.com/images/icons/emoji/octocat.png)

### Large image

![Branching](https://guides.github.com/activities/hello-world/branching.png)

### Center an image with Kramdown

![Octocat](https://assets-cdn.github.com/images/icons/emoji/octocat.png)

### Definition lists can be used with HTML syntax.

<dl>
<dt>Name</dt>
<dd>Godzilla</dd>
<dt>Born</dt>
<dd>1952</dd>
<dt>Birthplace</dt>
<dd>Japan</dd>
<dt>Color</dt>
<dd>Green</dd>
</dl>

```
Long, single-line code blocks should not wrap. They should horizontally scroll if they are too long. This line should be long enough to demonstrate this.
```

```
The final element.
```
