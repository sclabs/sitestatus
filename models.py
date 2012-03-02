from google.appengine.ext import db

# represents the status of a site and associated information
class Status(db.Model):
    # short description of the site
    description = db.StringProperty()

    # comment about the site
    comment = db.StringProperty()
    
    # link to the site
    link_url = db.StringProperty()

    # link display text
    link_text = db.StringProperty()

    # update information
    # should we check the status, title, or contents of the webpage?
    update_type = db.StringProperty(default='none',
                                    choices=set(['status', 'title', 'content', 'none']))

    # if contents, what should we look for in the contents?
    update_content = db.StringProperty()

    # if title, what should we look for in the title
    update_title = db.StringProperty()

    # url we should use to check the service
    update_url = db.StringProperty()

    # the status of the site
    status = db.StringProperty()
