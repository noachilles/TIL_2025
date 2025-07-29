const fetchUserData = (userId, callback) => {
  const xhr = new XMLHttpRequest()
  xhr.open('GET', `https://jsonplaceholder.typicode.com/users/${userId}`)
  xhr.send()
  xhr.onload = function () {
      if (xhr.status == 200) {
          callback(null, JSON.parse(xhr.responseText))
      } else {
          callback('Request failed')
      }
  }
}

const fetchUserPosts = (userId, callback) => {
  const xhr = new XMLHttpRequest()
  xhr.open('GET', `https://jsonplaceholder.typicode.com/posts?userId=${userId}`)
  xhr.send()
  xhr.onload = function () {
      if (xhr.status == 200) {
          callback(null, JSON.parse(xhr.responseText))
      } else {
          callback('Request failed')
      }
  }
}

const fetchPostComments = (postId, callback) => {
  const xhr = new XMLHttpRequest()
  xhr.open('GET', `https://jsonplaceholder.typicode.com/comments?postId=${postId}`)
  xhr.send()
  xhr.onload = function () {
      if (xhr.status == 200) {
          callback(null, JSON.parse(xhr.responseText))
      } else {
          callback('Request failed')
      }
  }
}

// Callback Hell example
fetchUserData(1, (error, user) => {
  if (error) {
      console.error(error)
  } else {
      fetchUserPosts(user.id, (error, posts) => {
          if (error) {
              console.error(error)
          } else {
              fetchPostComments(posts[0].id, (error, comments) => {
                  if (error) {
                      console.error(error)
                  } else {
                      console.log('User:', user)
                      console.log('Posts:', posts)
                      console.log('Comments:', comments)
                  }
              })
          }
      })
  }
})
