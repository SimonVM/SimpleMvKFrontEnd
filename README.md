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
