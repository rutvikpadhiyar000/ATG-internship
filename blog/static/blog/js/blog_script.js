let allSummaries = document.getElementsByClassName('post-desc')

for (let index = 0; index < allSummaries.length; index++) {
    const element = allSummaries[index];
    let elementText = element.textContent.split(" ")
    if (elementText.length > 15) {
        elementText = elementText.splice(0, 15)
        elementText.push('...')
        elementText = elementText.join(' ')
        element.textContent = elementText
    }
    
}