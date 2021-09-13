console.log('its working')

let theme = localStorage.getItem('theme')

if (theme == null){
	setTheme('light')
}
else{
	setTheme(theme)
}

let themeDots = document.getElementsByClassName('theme-dot')

console.log(themeDots.length)

for (var i = 0; i < themeDots.length; i++) {
	themeDots[i].addEventListener('click', function(){
		let mode = this.dataset.mode
		console.log('Option clicked : ', mode)
		setTheme(mode)
	})
}



function setTheme(mode) {
	if (mode == 'light') {
		document.getElementById('theme-style').href = '/static/Styles/default.css'
		console.log(document.getElementById('theme-style').href)

	}

	if (mode == 'dark') {
		document.getElementById('theme-style').href = '/static/Styles/dark.css'
		console.log(document.getElementById('theme-style').href)
	}

	if (mode == 'green') {
		document.getElementById('theme-style').href = 'green.css'
	}

	if (mode == 'purple') {
		document.getElementById('theme-style').href = 'purple.css'
	}
	
	localStorage.setItem('theme', mode)
}