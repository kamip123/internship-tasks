function getData() {
    let url = 'https://www.reddit.com/r/funny.json';

    fetch(url)
        .then(res => res.json())
        .then((out) => {
            data = out;
            setup();
        })
        .catch(err => {
            throw err
        });
}

function getPostData() {
    let count = 0;
    data.data.children.forEach(function (post) {
        let newPost = {
            "title": post.data.title,
            "upvotes": post.data.ups,
            "downvotes": post.data.downs,
            "score": post.data.score,
            "num_comments": post.data.num_comments,
            "created": post.data.created
            //"created": new Date(post.data.created) todo
        };
        posts.posts.push(newPost);
        count++;
    });
    posts.count = count;
}

function updateTable() {
    let table = document.getElementById('posts_tbody');
    table.innerHTML = '';
    let tempCounter = 1;
    for (let key in posts.posts) {
        let newTr = document.createElement("tr");
        let counterTd = document.createElement("th");
        counterTd.innerHTML = tempCounter + '.';
        newTr.appendChild(counterTd);
        for (let value in posts.posts[key]) {

            if (value === 'created') {
                let newTd = document.createElement("td");
                newTd.innerHTML = new Date(posts.posts[key][value] * 1000);
                newTr.appendChild(newTd);
            } else {
                let newTd = document.createElement("td");
                newTd.innerHTML = posts.posts[key][value];
                newTr.appendChild(newTd);
            }
        }
        table.appendChild(newTr);
        tempCounter++;
    }
}

function sortTable(columnName) {
    let newPosts = [];

    if (sortedBy !== 'nothing') {
        if (sortedBy === columnName) {
            ascOrDesc = -ascOrDesc;
        } else {
            sortedBy = columnName;
            ascOrDesc = 1;
        }
    } else {
        sortedBy = columnName;
        ascOrDesc = 1;
    }

    for (let key in posts.posts) {
        newPosts.push(posts.posts[key]);
    }

    if (ascOrDesc === 1) {
        switch (columnName) {
            case 'title':
                newPosts.sort(function (a, b) {
                    let temp_a = a.title.toLowerCase(), temp_b = b.title.toLowerCase();
                    if (temp_a < temp_b)
                        return -1;
                    if (temp_a > temp_b)
                        return 1;
                    return 0;
                });
                break;
            case 'upVotes':
                newPosts.sort(function (a, b) {
                    return a.upvotes - b.upvotes
                });
                break;
            case 'downVotes':
                newPosts.sort(function (a, b) {
                    return a.downvotes - b.downvotes
                });
                break;
            case 'score':
                newPosts.sort(function (a, b) {
                    return a.score - b.score
                });
                break;
            case 'comments':
                newPosts.sort(function (a, b) {
                    return a.num_comments - b.num_comments
                });
                break;
            case 'created':
                newPosts.sort(function (a, b) {
                    return a.created - b.created
                });
                break;
        }
    } else {
        switch (columnName) {
            case 'title':
                newPosts.sort(function (a, b) {
                    let temp_a = a.title.toLowerCase(), temp_b = b.title.toLowerCase();
                    if (temp_a < temp_b)
                        return 1;
                    if (temp_a > temp_b)
                        return -1;
                    return 0;
                });
                break;
            case 'upVotes':
                newPosts.sort(function (a, b) {
                    return b.upvotes - a.upvotes
                });
                break;
            case 'downVotes':
                newPosts.sort(function (a, b) {
                    return b.downvotes - a.downvotes
                });
                break;
            case 'score':
                newPosts.sort(function (a, b) {
                    return b.score - a.score
                });
                break;
            case 'comments':
                newPosts.sort(function (a, b) {
                    return b.num_comments - a.num_comments
                });
                break;
            case 'created':
                newPosts.sort(function (a, b) {
                    return b.created - a.created
                });
                break;
        }
    }

    let table = document.getElementById('posts_tbody');
    table.innerHTML = '';
    let tempCounter = 1;
    for (let post in newPosts) {
        let newTr = document.createElement("tr");
        let counterTd = document.createElement("th");
        counterTd.innerHTML = tempCounter + '.';
        newTr.appendChild(counterTd);
        for (let value in newPosts[post]) {
            if (value === 'created') {
                let newTd = document.createElement("td");
                newTd.innerHTML = new Date(newPosts[post][value] * 1000);
                newTr.appendChild(newTd);
            } else {
                let newTd = document.createElement("td");
                newTd.innerHTML = newPosts[post][value];
                newTr.appendChild(newTd);
            }
        }
        table.appendChild(newTr);
        tempCounter++;
    }

}

function searchRecent() {
    let newPosts = [];
    let last24h = Math.floor(Date.now() / 1000) - (24 * 60 * 60);

    for (let key in posts.posts) {
        if (posts.posts[key]['created'] >= last24h) {
            newPosts.push(posts.posts[key]);
        }
    }

    let table = document.getElementById('posts_tbody');
    table.innerHTML = '';
    let tempCounter = 1;
    for (let post in newPosts) {
        let newTr = document.createElement("tr");
        let counterTd = document.createElement("th");
        counterTd.innerHTML = tempCounter + '.';
        newTr.appendChild(counterTd);
        for (let value in newPosts[post]) {
            if (value == 'created') {
                let newTd = document.createElement("td");
                newTd.innerHTML = new Date(newPosts[post][value] * 1000);
                newTr.appendChild(newTd);
            } else {
                let newTd = document.createElement("td");
                newTd.innerHTML = newPosts[post][value];
                newTr.appendChild(newTd);
            }
        }
        table.appendChild(newTr);
        tempCounter++;
    }
}

function addListeners() {

    ///////// table head

    let title = document.getElementById('title');
    title.addEventListener('click', function () {
        sortTable('title')
    });

    let upVotes = document.getElementById('upVotes');
    upVotes.addEventListener('click', function () {
        sortTable('upVotes')
    });

    let downVotes = document.getElementById('downVotes');
    downVotes.addEventListener('click', function () {
        sortTable('downVotes')
    });

    let score = document.getElementById('score');
    score.addEventListener('click', function () {
        sortTable('score')
    });

    let comments = document.getElementById('comments');
    comments.addEventListener('click', function () {
        sortTable('comments')
    });

    let created = document.getElementById('created');
    created.addEventListener('click', function () {
        sortTable('created')
    });

    ///////// buttons

    let titleButton = document.getElementById('titleButton');
    titleButton.addEventListener('click', function () {
        sortTable('title')
    });

    let upVotesButton = document.getElementById('upVotesButton');
    upVotesButton.addEventListener('click', function () {
        sortTable('upVotes')
    });

    let downVotesButton = document.getElementById('downVotesButton');
    downVotesButton.addEventListener('click', function () {
        sortTable('downVotes')
    });

    let scoreButton = document.getElementById('scoreButton');
    scoreButton.addEventListener('click', function () {
        sortTable('score')
    });

    let commentsButton = document.getElementById('commentsButton');
    commentsButton.addEventListener('click', function () {
        sortTable('comments')
    });

    let createdButton = document.getElementById('createdButton');
    createdButton.addEventListener('click', function () {
        sortTable('created')
    });

    ///////// special buttons

    let searchBy24h = document.getElementById('searchBy24h');
    searchBy24h.addEventListener('click', searchRecent);
}

function setup() {
    getPostData();
    updateTable();
    addListeners();
}


let data;
let posts = {"count": 0, "posts": []};
let sortedBy = 'nothing';
let ascOrDesc = 1;
window.onload = getData;

// todo
// data
// 3) napisać funkcję, która zwróci tytuł postu z najwyższym stosunkiem głosów dodatnich i ujemnych (w przypadku kilku postów o jednakowych współczynnikach, wybrać najnowszy z nich)
// 4) napisać funkcję, która wyświetli posty tylko z ostatniego dnia (24h wstecz)
// zrobic readme
// napisac testy