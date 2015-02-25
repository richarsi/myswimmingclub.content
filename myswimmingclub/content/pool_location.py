from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Item

from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder

from plone.supermodel import model
from Products.Five import BrowserView

from myswimmingclub.content import MessageFactory as _
from myswimmingclub.content.swimming_meet import ISwimmingMeet

API_KEY=u'getYourAPIKeyFromGoogle'

# Interface class; used to define content-type schema.

class IPoolLocation(model.Schema, IImageScaleTraversable):
    """
    Pool Location content type for My Swimming Club
    """

    # If you want a schema-defined interface, delete the model.load
    # line below and delete the matching file in the models sub-directory.
    # If you want a model-based interface, edit
    # models/pool_location.xml to define the content type.

    model.load("models/pool_location.xml")


# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class PoolLocation(Item):

    # Add your class methods and properties here
    pass


# View class
# The view is configured in configure.zcml. Edit there to change
# its public name. Unless changed, the view will be available
# TTW at content/@@sampleview

class PoolLocationView(BrowserView):
    """ pool location view class """

    # Add view methods here
    def sessions(self):
        """Return a catalog search result of sessions to show
        """

        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')

        return catalog(object_provides=ISwimmingMeet.__identifier__,
                       path='/'.join(context.getPhysicalPath()),
                       sort_on='sortable_title')


    def getGoogleIframeSrc(self):
        """Return a string representation of the google query to use in
           an iframe
        """

        src="https://www.google.com/maps/embed/v1/place?key=%s&amp;q=%s \
          &amp;attribution_source=Google+Maps+Embed+API \
          &amp;attribution_web_url=http://www.copsclub.co.uk/"
        return src
