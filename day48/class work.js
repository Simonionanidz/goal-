function updateProfile() {
    var firstName = document.getElementById('firstName').value;
    var lastName = document.getElementById('lastName').value;
    var group = document.getElementById('group').value;

    document.getElementById('firstNameDisplay').innerText = firstName;
    document.getElementById('lastNameDisplay').innerText = lastName;
    document.getElementById('groupDisplay').innerText = group;
}

function resetProfile() {
    document.getElementById('firstName').value = '';
    document.getElementById('lastName').value = '';
    document.getElementById('group').value = '';
    document.getElementById('firstNameDisplay').innerText = '';
    document.getElementById('lastNameDisplay').innerText = '';
    document.getElementById('groupDisplay').innerText = '';
}