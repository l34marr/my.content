# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from my.content import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.autoform import directives
from plone.formwidget.autocomplete.widget import AutocompleteFieldWidget
from plone.app.textfield import RichText
from crgis.atcontents.interfaces.temple import ITemple
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm


reged = SimpleVocabulary(
    [SimpleTerm(value=u'y', title=_(u'Yes')),
     SimpleTerm(value=u'n', title=_(u'No'))]
)

reglvl = SimpleVocabulary(
    [SimpleTerm(value=u'n', title=_(u'National')),
     SimpleTerm(value=u'm', title=_(u'Municipal')),
     SimpleTerm(value=u'c', title=_(u'County'))]
)

ritectgr = SimpleVocabulary(
    [SimpleTerm(value=u'perf', title=_(u'Performance')),
     SimpleTerm(value=u'work', title=_(u'ArtWork')),
     SimpleTerm(value=u'oral', title=_(u'Oral')),
     SimpleTerm(value=u'knwd', title=_(u'Knowledge')),
     SimpleTerm(value=u'none', title=_(u'None'))]
)


class IMyContentLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IFolklore(Interface):

    id = schema.TextLine(
        title=_(u'Census ID'),
    )

    c_start = schema.Date(
        title=_(u'Census Start'),
    )

    c_end = schema.Date(
        title=_(u'Census End'),
    )

    c_org = schema.TextLine(
        title=_(u'Census Organization'),
    )

    c_prsn = schema.TextLine(
        title=_(u'Census Person'),
    )

    title = schema.TextLine(
        title=_(u'Title'),
        required=True,
    )

    description = schema.Text(
        title=_(u'Description'),
        required=False,
    )

    title_a = schema.TextLine(
        title=_(u'Title Used'),
        required=False,
    )

    title_b = schema.TextLine(
        title=_(u'Title Other'),
        required=False,
    )

    reged = schema.Choice(
        title=_(u'Registed'),
        required=True,
        vocabulary=reged,
    )

    reglvl = schema.Choice(
        title=_(u'Reg Level'),
        required=False,
        vocabulary=reglvl,
    )

    ethnic = schema.Tuple(
        title=_(u'Ethnic'),
        description=_(u'One Value Per Line'),
        required=False,
        value_type=schema.TextLine(),
        missing_value=(),
    )

    xingtai = schema.Tuple(
        title=_(u'XingTai'),
        description=_(u'One Value Per Line'),
        required=False,
        value_type=schema.TextLine(),
        missing_value=(),
    )

    during = schema.TextLine(
        title=_(u'During'),
        required=False,
    )

    freq = schema.TextLine(
        title=_(u'Frequence'),
        required=False,
    )

    area_adm = schema.TextLine(
        title=_(u'AreaAdm'),
        required=False,
    )

    area_trd = schema.TextLine(
        title=_(u'AreaTrd'),
        required=False,
    )

    status = schema.TextLine(
        title=_(u'Status'),
        required=False,
    )

    histrk = schema.Text(
        title=_(u'History Tracking'),
        required=False,
    )

    rite_prg = schema.Text(
        title=_(u'Rite Progress'),
        required=False,
    )

    rite_ftr = schema.Text(
        title=_(u'Rite Feature'),
        required=False,
    )

    rite_ctg = schema.Choice(
        title=_(u'Rite Category'),
        required=True,
        vocabulary=ritectgr,
    )

    rite_spc = schema.Text(
        title=_(u'Rite Space'),
        required=False,
    )

    rite_itm = schema.Text(
        title=_(u'Rite Item'),
        required=False,
    )

    perf_ngo = schema.Text(
        title=_(u'Performer NonGov'),
        required=False,
    )

    perf_grp = schema.Text(
        title=_(u'Performer Group'),
        required=False,
    )

    perf_ref = RichText(
        title=_(u'Performer Reference'),
        required=False,
    )

    perf_dat = RichText(
        title=_(u'Performer Data'),
        required=False,
    )

    photo = RichText(
        title=_(u'Photo Image'),
        required=False,
    )

    directives.widget('temple', AutocompleteFieldWidget)
    temple = RelationChoice(
        title=_(u'Related Temple'),
        source=ObjPathSourceBinder(
            object_provides=ITemple.__identifier__,
            navigation_tree_query={'path': {'query': '/Plone/temples'}},
        ),
        required=False,
    )

