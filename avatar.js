document.addEventListener('DOMContentLoaded', function() {
    var accountName = localStorage.getItem('username') || 'Guest';
    var accountNameSpan = document.getElementById('accountName');
    if (accountNameSpan) accountNameSpan.textContent = accountName;

    var avatars = [
        "https://cdn-icons-png.flaticon.com/512/147/147144.png",
        "https://cdn-icons-png.flaticon.com/512/1946/1946429.png",
        "https://cdn-icons-png.flaticon.com/512/2922/2922510.png",
        "https://cdn-icons-png.flaticon.com/512/2922/2922656.png",
        "https://cdn-icons-png.flaticon.com/512/2922/2922506.png",
        "https://cdn-icons-png.flaticon.com/512/2922/2922522.png",
        "https://cdn-icons-png.flaticon.com/512/2922/2922518.png",
        "https://cdn-icons-png.flaticon.com/512/4140/4140048.png",
        "https://cdn-icons-png.flaticon.com/512/4140/4140037.png",
        "https://cdn-icons-png.flaticon.com/512/4140/4140061.png",
        "https://cdn-icons-png.flaticon.com/512/4140/4140084.png",
        "https://cdn-icons-png.flaticon.com/512/616/616408.png",
        "https://cdn-icons-png.flaticon.com/512/616/616494.png",
        "https://cdn-icons-png.flaticon.com/512/616/616489.png",
        "https://cdn-icons-png.flaticon.com/512/616/616493.png",
        "https://cdn-icons-png.flaticon.com/512/616/616495.png",
        "https://cdn-icons-png.flaticon.com/512/616/616497.png",
        "https://cdn-icons-png.flaticon.com/512/616/616498.png",
        "https://cdn-icons-png.flaticon.com/512/616/616491.png",
        "https://cdn-icons-png.flaticon.com/512/616/616496.png",
        "https://cdn-icons-png.flaticon.com/512/616/616492.png",
        "https://cdn-icons-png.flaticon.com/512/616/616490.png"
    ];

    function getAvatarIndex(name) {
        let sum = 0;
        for (let i = 0; i < name.length; i++) sum += name.charCodeAt(i);
        return sum % avatars.length;
    }

    var avatarIndex = getAvatarIndex(accountName);
    var avatarImg = document.getElementById('avatarImg');
    if (avatarImg) avatarImg.src = avatars[avatarIndex];
});
