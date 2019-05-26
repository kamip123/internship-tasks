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
        };
        posts.posts.push(newPost);
        count++;
    });
    posts.count = count;
    console.log(posts);
}

function printTable(postList) {
    let table = document.getElementById('postsTbody');
    table.innerHTML = '';
    let tempCounter = 1;
    for (let post in postList) {
        let newTr = document.createElement("tr");
        let counterTd = document.createElement("th");
        counterTd.innerHTML = tempCounter + '.';
        newTr.appendChild(counterTd);
        for (let value in postList[post]) {
            if (value === 'created') {
                let newTd = document.createElement("td");
                let creationDate = new Date(postList[post][value] * 1000);
                let day = ('0' + creationDate.getDate()).slice(-2);
                let month = ('0' + (creationDate.getMonth() + 1)).slice(-2);
                let year = creationDate.getFullYear();
                let hour = ('0' + creationDate.getHours()).slice(-2);
                let minutes = ('0' + creationDate.getMinutes()).slice(-2);
                newTd.innerHTML = day + '.' + month + '.' + year + ' ' + hour + ':' + minutes;
                newTr.appendChild(newTd);
            } else {
                let newTd = document.createElement("td");
                newTd.innerHTML = postList[post][value];
                newTr.appendChild(newTd);
            }
        }
        table.appendChild(newTr);
        tempCounter++;
    }
}

function updateTable() {
    let loading = document.getElementById('loadingHeader');
    loading.innerHTML = '';
    printTable(posts.posts);
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

    printTable(newPosts);
}

function searchRecent() {
    let newPosts = [];
    let currentH = Math.floor(Date.now() / 1000);
    let last24h = Math.floor(Date.now() / 1000) - (24 * 60 * 60);

    for (let key in posts.posts) {
        if (posts.posts[key]['created'] >= last24h && posts.posts[key]['created'] <= currentH) {
            newPosts.push(posts.posts[key]);
        }
    }

    printTable(newPosts);
}

function searchBestCommentUpsRatio() {
    let max_value = 0;
    let index;

    for (let key in posts.posts) {
        let ratio = posts.posts[key]['upvotes'] / posts.posts[key]['num_comments']
        if (ratio > max_value) {
            max_value = ratio
            index = key
        }
    }
    let result = document.getElementById('result_p');
    result.innerHTML = String(posts.posts[index]['title']) + ' with ratio: ' + String(Math.round(max_value)) + ":1";
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

    let searchBestRatio = document.getElementById('searchBestRatio');
    searchBestRatio.addEventListener('click', searchBestCommentUpsRatio);
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

