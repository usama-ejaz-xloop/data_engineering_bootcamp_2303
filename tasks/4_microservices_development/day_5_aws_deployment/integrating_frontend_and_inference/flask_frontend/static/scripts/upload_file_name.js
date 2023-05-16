document.addEventListener('DOMContentLoaded', () => {
    let fileInputs = document.querySelectorAll('.file.has-name')
    for (let fileInput of fileInputs) {
        let input = fileInput.querySelector('.file-input')
        let name = fileInput.querySelector('.file-name')
        input.addEventListener('change', () => {
        let files = input.files
        if (files.length === 0) {
            name.innerText = 'No file selected'
        } else {
            name.innerText = files[0].name
        }
        })
    }
    })