let data;
let posts = {"count": 0, "posts": []};

QUnit.module("Data validation", {
    before: function () {
        return new Promise( function( resolve, reject ) {
            let url = 'https://www.reddit.com/r/funny.json';
            fetch(url)
                .then(res => res.json())
                .then((out) => {
                    data = out;

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
                    resolve();
                })
                .catch(err => {
                    reject( err );
                });
        } );
    }
});

QUnit.test('Posts count value', function( assert ) {
    assert.equal( posts.count, 26, 'Value should be 26' );
});

QUnit.test('Amount of posts recived - array length', function( assert ) {
    assert.equal( posts.posts.length, 26, 'Value should be 26' );
});

QUnit.test('Score not 0', function( assert ) {
    assert.ok( function( ){
        return posts.posts[0].score > 0;
    }, 'Value should be bigger than 0 and is ' + String(posts.posts[0].score) );
});

QUnit.test('Sort validation time asc', function( assert ) {
    let newPosts = sortTable('created', 1);
    console.log(newPosts);
    assert.ok( function(){
        return newPosts[0].created < newPosts[1].created
    }, 'The first value should be smaller than the second one: ' + String(newPosts[0].created) + ' < ' + String(newPosts[1].created) );
});

QUnit.test('Sort validation score asc', function( assert ) {
    let newPosts = sortTable('score', 1);
    console.log(newPosts);
    assert.ok( function(){
        return newPosts[0].score < newPosts[1].score
    }, 'The first value should be smaller than the second one: ' + String(newPosts[0].score) + ' < ' + String(newPosts[1].score) );
});

function sortTable(columnName, ascOrDesc) {
    let newPosts = [];

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

    return newPosts;
}
