from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField("Title", max_length=1000, null=True)
    def __str__(self):
        return '%s' % self.name
        
    class Meta:
        verbose_name = "Product categories"
        verbose_name_plural = "Product categories"
        
class Product(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('Disabled', 'Disabled')
    )
    YES_NO = (
        ('YES', 'YES'),
        ('NO', 'NO')
    )
    DISCOUNT = (
        ('0', '0'), ('5', '5'), ('10', '10'), ('15', '15'), ('20', '20'), ('25', '25'), ('30', '30'), ('35', '35'), ('40', '40'), ('45', '45'), ('50', '50'), ('55', '55'), ('60', '60'), ('65', '65'), ('70', '70'), ('75', '75'), ('80', '80'), ('85', '85'), ('90', '90'), ('95', '95')
    )
    GUARANTEE = (
        ('1 day', '1 day'),
        ('2 days', '2 days'), 
        ('3 days', '3 days'), 
        ('1 week', '1 week'),
        ('14 days', '14 days'),
        ('1 month', '1 month'),
        ('3 months', '3 months'),
        ('1 year', '1 year'),
        ('Eternal', 'Eternal'), 
        ('NO', 'NO')
    )
    KEY_ACCOUNT = (
        ('KEY', 'KEY'), 
        ('ACCOUNT', 'ACCOUNT')
    )
    name = models.CharField("Title", max_length=1000, null=True)
    description = models.TextField("Description", max_length=50000, null=True, default="NONE")
    notes = models.TextField("Notes", max_length=50000, null=True, default="NONE")
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.SET_NULL, null=True)
    status = models.CharField("Status", max_length=50, null=True, choices=STATUS)
    key_account = models.CharField("Key or account?", max_length=50, null=True, choices=KEY_ACCOUNT)
    email = models.CharField("Mail availability", max_length=50, null=True, choices=YES_NO)
    new = models.CharField("New?", max_length=50, null=True, choices=YES_NO)
    discount = models.CharField("Discount (default=0)", max_length=50, null=True, choices=DISCOUNT, default=0)
    guarantee = models.CharField("Warranty", max_length=50, null=True, choices=GUARANTEE)

    price = models.IntegerField("Price", null=False, default=0)
    
    image = models.ImageField("Cover (16/9)", default="default_image.png", null=True, blank=True)

    data_created = models.DateField(auto_now_add=True, null=False)
    def __str__(self):
        return '%s' % self.name
        
    class Meta:
        verbose_name = "Products"
        verbose_name_plural = "Products"
        
class Gallery(models.Model):
    image = models.ImageField("Picture", upload_to='gallery')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    def __str__(self):
        return '%s' % self.product
        
    class Meta:
        verbose_name = "Gallery (Product photos)"
        verbose_name_plural = "Gallery (Product photos)"

class Slider(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self):
        return '%s' % self.product
        
    class Meta:
        verbose_name = "Slider on the home page"
        verbose_name_plural = "Slider on the home page"

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    creator = models.CharField("Author", max_length=50, null=False)
    text = models.TextField("Comment text", max_length=500, null=False)
    ip = models.CharField("Author's IP", max_length=100, null=False, default=0)
    data_created = models.DateField(auto_now_add=True, null=False)
    def __str__(self):
        return '%s' % self.text
        
    class Meta:
        verbose_name = "User comments"
        verbose_name_plural = "User comments"

class Settings(models.Model):
    YES_NO = (
        ('YES', 'YES'),
        ('NO', 'NO')
    )
    
    BUTTON_STYLE = (
        ('primary', 'primary'),
        ('secondary', 'secondary'),
        ('success', 'success'),
        ('danger', 'danger'),
        ('warning', 'warning'),
        ('info', 'info'),
        ('light', 'light'),
        ('dark', 'dark'),
    )
    
    name = models.CharField("Configuration name", max_length=50, null=False, default="Site settings")
    
    background = models.CharField("Site background", max_length=50, null=False, default="#f2edf3")
    
    slyder = models.CharField("Slider on the home page", max_length=50, null=True, choices=YES_NO, default="YES")
    
    loader = models.CharField("Website loading animation", max_length=50, null=True, choices=YES_NO, default="YES")
    loader_time = models.CharField("Site load time", max_length=50, null=False, default="2500")
    
    animation = models.CharField("Speed of animations on the site", max_length=50, null=False, default="1200")
    
    ico_image = models.ImageField("Website icon in the browser bar (16x16)", default="default_ico.ico", null=True, blank=True)
    logo_image = models.ImageField("Site logo", default="default_logo.svg", null=True, blank=True)
    logo_image_width = models.CharField("Site logo (width)", max_length=50, null=False, default="35")
    logo_text = models.CharField("Text next to the logo", max_length=50, null=False, default="Shop")
    ban_image = models.ImageField("Photo on the ban page", default="default_ban.png", null=True, blank=True)
    
    support = models.CharField("Feedback (Icon next to the logo)", max_length=50, null=True, choices=YES_NO, default="NO")
    
    buttons_style = models.CharField("Website buttons color", max_length=50, null=True, choices=BUTTON_STYLE, default="success")
    
    key_color = models.CharField("KEY icon settings\nKey icon color", max_length=100, null=False, default="#EB2F83")
    border_key = models.CharField("Frame color", max_length=100, null=False, default="#EB2F83")
    background_key = models.CharField("Background color", max_length=100, null=False, default="#fff")
    border_radius_key = models.CharField("Border radius", max_length=100, null=False, default="1rem")
    padding_top_bottom_key = models.CharField("Padding top + bottom", max_length=100, null=False, default="8px")
    padding_left_right_key = models.CharField("Padding left + right", max_length=100, null=False, default="10px")
    
    def __str__(self):
        return '%s' % self.name
        
    class Meta:
        verbose_name = "Site settings"
        verbose_name_plural = "Site settings" 
        
class Support(models.Model):
    text  = models.TextField("Message text", max_length=500, null=False)
    user_support = models.CharField("Contacts for communication with the user", max_length=50, null=False)
    answer = models.TextField("Administration response", max_length=5000, null=False)
    ip = models.CharField("User IP", max_length=100, null=False, default=0)
    data_created = models.DateField(auto_now_add=True, null=False)
    def __str__(self):
        return '%s' % self.text
        
    class Meta:
        verbose_name = "User requests"
        verbose_name_plural = "User requests"

class Messenger(models.Model):
    name = models.CharField("Social network name", max_length=100, null=False)
    link = models.CharField("Link", max_length=1000, null=False)
    icon = models.CharField("Icon (fontawesome.com)", max_length=100, null=False)
    color = models.CharField("Icon color", max_length=100, null=False)
    size = models.CharField("Icon size", max_length=100, null=False, default="22px")
    def __str__(self):
        return '%s' % self.name
        
    class Meta:
        verbose_name = "Social networks (Feedback)"
        verbose_name_plural = "Social networks (Feedback)"

class Ban(models.Model):
    ip = models.CharField("Intruder's IP address", max_length=100, null=False)
    why = models.CharField("Block reason", max_length=1000, null=False)
    def __str__(self):
        return '%s' % self.ip
        
    class Meta:
        verbose_name = "Block user by IP"
        verbose_name_plural = "Block user by IP"

class FAQ(models.Model):
    text = models.TextField("Section text", max_length=50000, null=False)
    def __str__(self):
        return '%s' % self.text
        
    class Meta:
        verbose_name = "FAQ (Shop rules)"
        verbose_name_plural = "FAQ (Shop rules)"