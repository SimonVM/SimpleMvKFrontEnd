SimpleMvKFrontEnd
=================

This is a front-end for the MvK written in TkInter. It's very basic, and resembles (not only visually) AToM³. It depends on the MvK project, so I suggest to run it in Eclipse, and make the project depend on MvK.

It offers the following functionality:

1. Create a Model: this opens a window, which allows you to navigate to the type model you want this model to conform to. Navigate through packages by double-clicking on them, then select a type model by clicking once on it. Press the SELECT button to actually create the model. A window will then pop up with the attributes you need to fill in for the model, as well as a location (which is a dot-separated string pointing to a location in the modelverse).

2. Load a type model: after creating a model, it's possible to load more type models. This is for instance necessary when creating a rule, because the contents of the LHS/NACs/RHS will conform to the RAMified type models.

3. (UNDER CONSTRUCTION) Load a model: loads a model from the modelverse.

4. Record all actions: will record all actions performed in a file called record.txt. Useful for replaying purposes.

5. Save the modelverse: serializes the contents of the modelverse to disk. If the front-end is started afterwards, it will automatically load this version of the modelverse.

Creating Elements
=================

Once a toolbar is loaded, types can be instantiated. Left-click on a type to select it, then right-click anywhere on the canvas to instantiate it.

Note that currently, there is only a default concrete syntax: the name of the element, followed by the name of the class it is an instance of.

When you instantiate a type, a window will pop up with the attributes to be given a value. Important to note is that usually, this is intuitive: for an integer attribute, you can fill in 0, 5, -1, ... For a boolean attribute, you can fill in True or False. However, if the type cannot be automatically deduced (such as when creating a SimpleClassDiagrams.Attribute, the Attribute.default value), you have to manually instantiate it, for example: IntegerValue(0).

You can edit instances by clicking on them with the middle mouse button. All attributes are listed, and you can give them new values. If you created an element, and that element's type is connected to another type though a composition, you can also add such children in this window. A good example is Class and Attribute from SimpleClassDiagram: when editing a Class, there is a button to add new Attributes through the attributes composition.

Creating Associations
=================

Associations are created just as Clabjects are. For example, when the SimpleClassDiagrams formalism is loaded, you can create the 'Inherits' association between two classes by left-clicking the correct button in the toolbar, then right-clicking anywhere on the canvas. The first two attributes will be the names of the association ends: in this case 'from_class' and 'to_class'. Here, you need to fill in the absolute path of the classes you want the inheritance relation to be created between. For example, 'from_class' can be 'formalisms.Petrinets.Place' and 'to_class' can be 'formalisms.Petrinets.NamedElement'. The rest of the attributes are filled in as with Clabjects.

Creating Attributes (in SimpleClassDiagrams)
=================

When a Clabject or Association is created, it can be edited by middle-clicking its visual representation on the canvas.

The edit screen will list all the attributes of the element, and allow to edit them. For each outgoing Composition relation of the element (in the case of SimpleClassDiagrams.Class, 'attributes' is the only outgoing Composition), it will list a separate button and a list of elements connected with it through that Composition.

The button allows to create an instance as a child of the element which is being edited. In the case of an attribute, the attribute will be created on the location of the element being edited, and a composition relation between the element and the attribute is automatically instantiated.

Attribute Values
=================
Usually, the system can infer the type of the attribute a value is assigned to. For example, the 'name' attribute of a Class is a String: so the system knows that it has to parse whatever value you assign to it as a String. The same is true for the lower bound of an Association: it knows to parse this as an integer.

Sometimes, however, the system cannot automatically deduce this. A good example is the 'default' attribute of an Attribute: this value can be of any type, and therefore it is impossible for the system to deduce which type actually has to be instantiated. For those cases, it's also possible to manually instantiate the correct class. In the 'default' example, you could enter 'StringValue('test')' or 'IntegerValue(0)'.
