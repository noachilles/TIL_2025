const fetchUserData = (userId) => {
    return new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest();
        xhr.open('GET', `https://jsonplaceholder.typicode.com/users/${userId}`);
        xhr.send();
        xhr.onload = function () {
            if (xhr.status == 200) {
                resolve(JSON.parse(xhr.responseText));
            } else {
                reject('Request failed');
            }
        };
        xhr.onerror = function () {
            reject('Request failed');
        };
    });
};

const fetchUserPosts = (userId) => {
    return new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest();
        xhr.open('GET', `https://jsonplaceholder.typicode.com/posts?userId=${userId}`);
        xhr.send();
        xhr.onload = function () {
            if (xhr.status == 200) {
                resolve(JSON.parse(xhr.responseText));
            } else {
                reject('Request failed');
            }
        };
        xhr.onerror = function () {
            reject('Request failed');
        };
    });
};

const fetchPostComments = (postId) => {
    return new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest();
        xhr.open('GET', `https://jsonplaceholder.typicode.com/comments?postId=${postId}`);
        xhr.send();
        xhr.onload = function () {
            if (xhr.status == 200) {
                resolve(JSON.parse(xhr.responseText));
            } else {
                reject('Request failed');
            }
        };
        xhr.onerror = function () {
            reject('Request failed');
        };
    });
};

// Using Promises
fetchUserData(1)
    .then(user => {
        console.log('User:', user);
        return fetchUserPosts(user.id);
    })
    .then(posts => {
        console.log('Posts:', posts);
        return fetchPostComments(posts[0].id);
    })
    .then(comments => {
        console.log('Comments:', comments);
    })
    .catch(error => {
        console.error(error);
    });
