# html-css-javascript

## Basics of HTML

### image

```html
<img src="stella_photo.jpg" width="300" /> # no height, browser automatically choose height by width
<img src="stella_photo.jpg" width="50%" />  # % is relative to the body/container/.. contains the image, called parent

```

### audio

```html
<audio src="beep.mp3" autoplay></audio> # autoplay
<audio src="beep.mp3" controls></audio> # play/pause/volume
<audio src="beep.mp3" autoplay loop></audio> # keep looping
```

#### handling new tags in older browsers

```html
<this_new_html_tag>
	<p>Sorry, your browser can't handle <i> this_new_html_tag </i>!</p>
</this_new_html_tag>
```

### video
similar to audio

```html
<video src="walking.mp4" autoplay></video>
<video src="walking.mp4" controls></video>
<video src="walking.mp4" loop></video>
<video src="walking.mp4" alt="walking through"></video> # for search engines and disabled people
```

### links

```html
<a href="https://www.gmail.com/">gmail</a>
<a href="https://twitter.com/"><img src="twitter
_icon.png"></a> #pic as anchoring link

```

#### a position within a page
* add `id="here"` to the element you will link to
* then use `<a href="#here">Go here</a>`
* from another web page use `<a href="page.html#here">Go here</a>`

### void elements
* no end tag
* `<meta name = "author">`
* `<img>`
* `<input>`
* `<br>`
* `<wbr>` - long word break
* `<hr>` - horizontal rule/line

---

### Style
* CSS : cascading style sheets
	* 1 CSS file used by multiple pages
	* `<link href="html_example.css" rel="stylesheet" type="text/css">`
	* class rules
		* `.classname {color: purple}`
	* inline style
		* higher priority
	* `pseudo-classes`
		* intelligence
		* `h1:hover {color: red}`
			* mouse movers over
		* `a:link {color: red}`
		* `a:visited {color: red}`
			* visited page
		* `a:active {color:red}`
			* currently being processed
		* `p:empty {color: red}`

### Tables
```html
<table>
		<thead>
				<tr> <th>...</th> <th>...</th> </tr>
		</thead>
		<tbody>
				<tr> <td>...</td> <td>...</td> </tr>
				<tr> <td>...</td> <td>...</td> </tr>
		</tbody>
</table>
```
multiple class

### div & span
* `div` no default style/meaning
	* absolute position
```html
<div style="position:absolute; top: 90px; left: 60px">
This is a div
</div>
```
	* relative position
  go down 20px then go left 20px
```html
<div style="position: relative; top: -20px; left: -20px">
This is a div
</div>
```
* `span` used for a few words
