function set_first() {
    let checkbox = document.getElementById('id_set_first');
    if (checkbox.checked) {
        let form = document.getElementById('image-form');
        let formData = new FormData(form);
        let url = form.action + '?set_first=True';
        fetch(url, {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (response.ok) {
                location.reload();
            } else {
                alert('Error: ' + response.statusText);
            }
        })
        .catch(error => {
            alert('Error: ' + error);
        });
    }
}
