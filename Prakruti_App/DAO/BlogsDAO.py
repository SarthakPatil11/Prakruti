from Prakruti_App.Utility.BlogData import BlogData
from Prakruti_App.models import Blogs


def GetAllBlogs():
    blogs = Blogs.objects.all()
    return blogs

def GetBlogByID(blogID):
    blog = Blogs.objects.get(id=blogID)
    return blog

def AddBlog(blogData: BlogData):
    new_blog = Blogs(Title=blogData.Title, Type=blogData.Type,
                    Content=blogData.Content, Date=blogData.Date, file=blogData.File)
    new_blog.save()
