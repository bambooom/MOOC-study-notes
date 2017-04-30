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
* style rule priority
	* more than one style rule, later one applies.
	* inline style rule always highest precedence


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

### Forms
* from browser to server

```html
<form action="destination" method="GET or POST">
	<input type="submit" value="submit">
</form>
```
* `destination`
	* server program `http://www.server.com/program.php`
	* on same server `dir/program.php`
	* same server same dir `program.php`

```html
<form>
	<input type="text" name="feedback"> <br>
	Please select each of the following that you have. <br>
	<input type="checkbox" name="items" value="car">
	<input type="checkbox" name="items" value="house">
	Please indicate yout intelligence level.<br>
	<input type="radio" name="iq" value="high">High <br>
	<input type="radio" name="iq" value="medium">Medium <br>
	<input type="radio" name="iq" value="low">Low <br>
</form>
```
* `radio` type means unique choice
* `type="password"` cannot use GET method
* dropdown menu cell
```html
<form>
	<select name="cities">
		<option value="hk">Hong Kong</option>
		<option value="ny">New York</option>
		<option value="sf">San Francisco</option>
	</select>
</form>
```

* useful attribute
	* `value="sth"`
	* `placeholder="sth"` - default text but disappear when user typing
	* `autofoxus` given focus to start field
	* `required` sets must fill in fields

```html
<label for="age">Age: </label>
<input type="text" id="age" name="age" required>
```
* `for` attribute corresponding to the `id` of `input`
* `name` used by server

#### file upload
```html
<form action="destination" method="post" enctype="part/form-data">
	<input type="file" name="file2upload">
	<input type="submit" value="upload the file">
</form>
```
server program may deal with the files.

#### input new elements
* `<input type="number">`
* `<input type="date">`
* `<input type="time">`
* `<input type="color">` color picker
* `<input type="range">` slider

#### elements grouping
* `<fieldset>` + `<legend>`
* visual way to grouping
* a box surrounding

#### `alt` text to an image
alt attributes, also known as alt text, are what browsers will display if they fail to load the image. alt attributes are also important for blind or visually impaired users to understand what an image portrays. And search engines also look at alt attributes.
```html
<img class="smaller-image thick-green-border" alt="A cute orange cat lying on its back" src="https://bit.ly/fcc-relaxing-cat">
```

#### Form element
```html
<form action="/submit-cat-photo">
	<input type="text" placeholder="cat photo URL">
	<button type="submit">submit</button>
</form>
```

#### radio buttons 单选
default checked
```html
<label><input type="radio" name="indoor-outdoor" checked> Indoor</label>
```

#### checkbox
default checked
```html
<label><input type="checkbox" name="personality" checked> Loving</label>
```
#### id attributes
除了name 还可以有 id, 在 jQuery 中会用到, id 的 CSS 也可在 style 中设置
```css
#cat-photo-element {
  background-color: green;
}
```

## Padding & Margin
padding: amount of space between the element and its border
上下?
margin: amount of space between an element's border and surrounding elements
上下左右都有?

```css
<style>
  .injected-text {
    margin-bottom: -25px;
    text-align: center;
  }

  .box {
    border-style: solid;
    border-color: black;
    border-width: 5px;
    text-align: center;
  }

  .yellow-box {
    background-color: yellow;
    padding: 10px;
  }

  .red-box {
    background-color: red;
    padding: 40px;
		margin: 20px;
  }

  .green-box {
    background-color: green;
    padding: 20px;
		margin: 20px;
  }
</style>
<h5 class="injected-text">margin</h5>

<div class="box yellow-box">
  <h5 class="box red-box">padding</h5>
  <h5 class="box green-box">padding</h5>
</div>
```

## Override Styles in Subsequent CSS
It doesn't matter which order the classes are listed in the HTML element.

However, the order of the class declarations in the <style> section are what is important. The second declaration will always take precedence over the first. Because .blue-text is declared second, it overrides the attributes of .pink-text

```html
<style>
  body {
    background-color: black;
    font-family: Monospace;
    color: green;
  }
  .pink-text {
    color: pink;
  }
  .blue-text {
    color: blue;
  }
</style>
<h1 class="pink-text blue-text">Hello World!</h1>
```

### id attributes always take precedence
```html
<style>
  body {
    background-color: black;
    font-family: Monospace;
    color: green;
  }
  .pink-text {
    color: pink;
  }
  .blue-text {
    color: blue;
  }
  #orange-text {
    color: orange;
  }
</style>
<h1 id="orange-text" class="pink-text blue-text">Hello World!</h1>
```
in-line style > id attributes > class came last

## Responsive Design with Bootstrap

#### Font Awesome
```html
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css"/>
```

#### Add a thumbs-up icon
```html
<i class="fa fa-thumbs-up"></i>
```

#### well class
Bootstrap has a class called well that can create a visual sense of depth for your columns.

## jQuery

#### script tag
code you put inside this function will run as soon as your browser has loaded your page.

This is important because without your document ready function, your code may run before your HTML is rendered, which would cause bugs.
```javascript
<script>
  $(document).ready(function() {
		$("button").addClass("animated bounce"); //Animate.css need, jQuery lib need
  });
</script>
```

jQuery often selects an HTML element with a selector, then does something to that element.
You see how we made all of your button elements bounce? We selected them with $("button"), then we added some CSS classes to them with .addClass("animated bounce");

three ways of targeting elements: by type: $("button"), by class: $(".btn"), and by id $("#target1")

jQuery has a function called .prop() that allows you to adjust the properties of elements.

#### change text inside an element using jQuery
jQuery has a function called .html() that lets you add HTML tags and text within an element. Any content previously within the element will be completely replaced with the content you provide using this function.

Here's how you would rewrite and emphasize the text of our heading:

$("h3").html("<em>jQuery Playground</em>");

jQuery also has a similar function called .text() that only alters text without adding tags. In other words, this function will not evaluate any HTML tags passed to it, but will instead treat it as text you want to replace with.
