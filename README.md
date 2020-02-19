[![Build Status](https://travis-ci.com/Funtext/Random-Memes.svg?branch=master)](https://travis-ci.com/Funtext/Random-Memes)

# Meme API

JSON API for a random meme scraped from reddit.

### Example Response:

```json
{
  "postLink": "https://redd.it/9vqgv2",
  "subreddit": "memes",
  "title": "Good mor-ning Reddit!...",
  "url": "https://i.redd.it/yykt3r9zsex11.png"
}
```

## Custom Endpoints

### Specify count (MAX 100)

In order to get multiple memes in a single request specify the count with the following endpoint.

Endpoint: [/{count}](https://rndmemes.herokuapp.com/2)

Example: https://rndmemes.herokuapp.com/2

Response:

```json
{
  "count": 2,
  "memes": [
    {
      "postLink": "https://redd.it/d5bn24",
      "subreddit": "meirl",
      "title": "meirl",
      "url": "https://i.redd.it/6wjb8gibu2n31.jpg"
    },
    {
      "postLink": "https://redd.it/d4zipy",
      "subreddit": "meirl",
      "title": "Me🚐irl",
      "url": "https://i.redd.it/hyl6fgweswm31.jpg"
    }
  ]
}
```

### Specify Subreddit

By default the API grabs a random meme from '_memes_', '_dankmemes_', '_meirl_' subreddits. To provide your own custom subreddit use the following endpoint.

Endpoint: [/{subreddit}](https://rndmemes.herokuapp.com/dankmemes)

Example: https://meme-api.herokuapp.com/gimme/dankmemes

### Specify Subreddit Count (MAX 100)

In order to get a custom number of memes from a specific subreddit provide the name of the subreddit and the count in the following endpoint.

Endpoint: [/{subreddit}/{count}](https://meme-api.herokuapp.com/gimme/dankmemes/2)

Example: https://rndmemes.herokuapp.com/dankmemes/2

Response:

```json
{
  "count": 2,
  "memes": [
    {
      "postLink": "https://redd.it/d5e119",
      "title": "Mph and km/h so everyone can understand",
      "url": "https://i.redd.it/imb4r0se74n31.jpg"
    },
    {
      "postLink": "https://redd.it/d5e5ns",
      "title": "Funnier as a team.",
      "url": "https://i.redd.it/ixb7absfa4n31.jpg"
    }
  ],
  "subreddit": "dankmemes"
}
```
