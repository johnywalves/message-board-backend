def postJSON(post):
    if post is not None:
        tags = []
        for tag in post.tags:
            tags.append({'name': tag.name})

        comments = []
        for comment in post.comments:
            comments.append({'id': comment.id, 'text': comment.text})

        return {'id': post.id, 'text': post.text, 'likes': post.likes, 'created_at': post.created_at.strftime('%Y-%m-%d %H:%M:%S'), 'tags': tags, 'comments': comments}
    else:
        return {}
