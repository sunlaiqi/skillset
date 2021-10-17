




# Running it as a web app
Flutter considers your browser to be a device when you’re running as a web app. So all that is needed to run as a web app is to enable the Google Chrome web browser as a device. You can enable it with this one-time command:
```bash
$ flutter config --enable-web
```
Setting "enable-web" value to "true".
From then on, when you get a list of devices on which to run your app, “Chrome” will appear as one of them. Simply choose to run your app in Chrome and the IDE will load your web app in it.

# Componentization

How would you go about doing that? Ponder that for a minute. Go ahead, we’ll wait.
Would you just start grabbing bricks and putting them together? Probably not. Would you lay out the soles of Thor’s feet and build from the bottom up? Again, no. Here’s my guess as to your common-sense strategy:
1. You’d get a vision of what you’re building. Figure the whole thing out.
2. Realize that the entire project is too complex to build at once.
3. Break the project into sections (legs, left arm, right arm, torso, left sword, right sword, helmet, cape, head).
4. Realize that each of them is still too complex.
5. For each section, you break it into sub-sections.
6. Repeat steps 4 and 5 until you’ve got simple enough components that each is easy to understand, build, and maintain – for you and for any teammates that you may have.
7. Create each simple component.
8. Combine simple components to form the larger, more complex components.
9. Repeat steps 7 and 8 until you’ve got your entire project created.
This process has a name: componentization, and is exactly the thought process we’ll go through with our Flutter projects.

The idea of recursively breaking down the complex bits into simpler bits is called **decomposition**. And the act of putting the written pieces back together into larger components is called **composition**.

In the world of Flutter, these components are referred to as widgets. Flutter people like to say “everything is widgets,” meaning that you and I will be using the Google-provided widgets – the ones that ship with Flutter. We’ll compose them together to create our own custom widgets. And our custom widgets will be composed together to create more and more complex custom widgets. This continues until you’ve got yourself a full-blown app.

Every app can be thought of in two parts:
1. **Behavior** – What the software does. All of the business logic goes here: the data reading, writing, and processing.
2. **Presentation** – How the software looks. The user interface. The buttons, textboxes, labels.
Only Flutter combines these into one language instead of two.

# UI as code

Developers use the same Dart language to express an app’s graphical user interface as well as the behavior. We call this “UI as code.”

So how does this UI get created? Like many other frameworks and languages, a flutter app starts with a main function. In Flutter, main will call a function called runApp(). This runApp() receives one widget, the root widget which can be named anything, but it should be a class that extends a Flutter StatelessWidget. It looks like this:
```dart
// import the Dart package needed for all Flutter apps
import 'package:flutter/material.dart';
// Here is main calling runApp
void main() => runApp(RootWidget());
// And here is your root widget
class RootWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Text("Hello world");
  } 
}
```

And that’s all you need to create a “Hello world” in Flutter.

# Built-in Flutter widgets

Flutter’s foundational widgets are the building blocks of everything we create and there are tons of them.
They fall into these major categories:

- Value widgets 
- Layout widgets 
- Navigation widgets 
- Other widgets

Every widget is a class that can have properties and methods. Every widget can have a constructor with zero or more parameters. And most importantly, every widget has a *build* method which receives a *BuildContext* and returns a single Flutter widget. If you’re ever wondering how a widget got to look the way it does, locate its *build* method:

```dart
class RootWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Text('Hello world');
  }
}
```
# Element Tree vs Virtual DOM

You may hear about a virtual DOM when other developers talk about Flutter. This comes from the world of React. (Remember that Flutter borrowed heavily from React’s excellent architecture.) Well, strictly speaking, Flutter doesn’t have a DOM, but it does maintain something resembling it – the element tree. The element tree is a tiny copy of all the widgets on the screen. Flutter maintains a current element tree and one with batched changes applied.

You see, Flutter might be really slow if it applied every tiny change to the screen and then tried to re-render it hundreds of times per second. Instead, Flutter applies all of those changes to a copy of the element tree. It then periodically “diffs” the current element tree with the modified one and decides what truly needs to be re-rendered. It only re-renders those parts that need it. This is much, much faster.

# Which one should I create (stateless vs statefull)?

The short answer is create a stateless widget. Never use a stateful widget until you must. Assume all widgets you make will be stateless and start them out that way. Refactor them into stateful widgets when you’re sure you really do need state. But recognize that state can be avoided more often than developers think. Avoid it when you can to make widgets simpler and therefore easier to write, to maintain, and to extend. Your team members will thank you for it.

Note there is actually a third type of widget, the inheritedWidget. you set a value in your inheritedWidget and any descendent can reach back up through the tree and ask for that data directly.

# Laying Out Your Widgets

So to get us where we need to be, we really must know how to do five things:
1. Layout the entire screen (aka scene)
This is where we’ll set the look and feel of the entire app and create the structure of the scene like the title, action button, and menus.

2. Position widgets above and below each other or side by side
When designing any scene, we break it into widgets and place them on the screen. 

A **ListView** can place widgets above and below each other.
How do you get the text next to the image? We’ll use a **Row widget**. 
How do you get the text above and below? We’ll use a **Column widget** there.

3. Handle extra space in the scene
Hey, there’s extra space on the right side of each Person. What if we wanted that space to be on the left? Or what if we wanted to put some of that extra space on the left of the image?

4. Handle situations when we run out of space and overflow the scene
In the scene with all of the PersonCards, we have more people than we have screen so we’ve overflowed it. This normally throws an error, but there are several ways to fix the situation. We’ll look at the best way.

5. Make finer adjustments in positioning
Our scene currently feels crowded. What can we do to create a little elbow room?

To turn on visual debugging in VS code (these visual cues will help you see how Flutter thinks so you can tune your layout).
In VS Code open the command palette (cmd-shift-P or control-shift-P) and type in “Toggle debug painting.”

## MaterialApp widget

The MaterialApp widget creates the outer framework for your app. 
- As important as it is, the user never sees the MaterialApp because no parts of it are technically visible. 
- It wraps your entire app, giving you the opportunity to give it a title so that when your OS moves the app into the background, it’ll have a name. 
- This is also where you’ll apply the default theme for your app – fonts, sizes, colors, and so forth. 
- MaterialApp is also the place to specify routes.
- Finally, MaterialApp has a home property. Remember that your project will have lots of custom widgets. You specify which one is the startup widget by **setting your MaterialApp’s home property**. This widget will be the root of your main scene and will therefore probably begin with a **Scaffold widget**. 

```dart
Widget build(BuildContext context) {
  return MaterialApp(
    home: MainWidget(),
    title: "Ch 6 Layouts",
    theme: ThemeData(primarySwatch: Colors.deepPurple),
    routes: <String, WidgetBuilder>{
      '/scene1': (BuildContext ctx) => MyWidget1(),
      '/scene2': (BuildContext ctx) => MyWidget2(),
      '/scene3': (BuildContext ctx) => MyWidget3(),
},
    debugShowCheckedModeBanner: false,
  );
}
```

## The Scaffold widget

Whereas the MaterialApp widget creates the **outer invisible framework**, the Scaffold widget creates the **inner visible framework**.
Scaffold has one purpose in life: to lay out the visible structure of your app to give it the predictable and therefore usable layout that so many other apps have. It creates, among other things:
- An AppBar for the title
- A section for the body
- A navbar at the bottom or a navigation drawer to the left
- A floating action button
- A bottom sheet – a section that is usually collapsed but can be slid up to reveal context-aware information for the scene that the user is on at that moment

```dart
@override
Widget build(BuildContext context) {
  return Scaffold(
    appBar: MyAppBar(),
    drawer: MyNavigationDrawer(),
    body: TheRealContentOfThisPartOfTheApp(),
    floatingActionButton: FloatingActionButton(
      child: Icon(Icons.add),
      onPressed: () { /* Do things here */},
    ),
    bottomNavigationBar: MyBottomNavBar,
  );
}
```
All parts of the Scaffold are optional.

## The AppBar widget

To create a header bar at the top of the screen, use an AppBar widget.
You’ll almost always have a title. And you may want to add an Icon at the start. An Icon is the leading property:

```dart
return Scaffold(
  appBar: AppBar(
      leading: Icon(Icons.traffic),
      title: Text("My Cool App"),
  ),
  /* More stuff here. FAB, body, drawer, etc. */
);
```
If you have a navigation drawer, you’re probably going to want to omit the leading icon.

## SafeArea widget

Device screens are seldom neat rectangles. They have rounded corners and notches and status bars at the top. If we ignored those things, certain parts of our app would be cut off or hidden. 

Simply wrap the SafeArea widget around all of your body content and let it do the heavy lifting for you. Putting it inside the Scaffold but around the body is a terrific place:

```dart
return Scaffold(
  drawer: LayoutDrawer(),
  body: SafeArea(
    child: MyNormalBody(),
  ),
  floatingActionButton: FloatingActionButton(
    child: Icon(Icons.next),
    onPressed: () {},
  ), 
);
```

## How Flutter decides on a widget’s size

In Flutter, every widget on your device’s screen eventually has a height and a width which it calls the “RenderBox.” Each widget also has constraints: a minHeight, a minWidth, a maxHeight, and a maxWidth which it calls the “BoxConstraints.”

As long as the widget’s RenderBox is completely within its BoxConstraints, life is good. 

## Flutter’s layout algorithm
In your custom widget, you have a root widget at the top of your main method. It has branches and branches of branches and on and on. Let’s call this the widget tree. Flutter has to decide how big to make each widget in the tree. It does so by asking each widget how big it would prefer to be and asking its parent if that is okay.

# Row and Column Widgets

```dart
Row(
  children: <Widget>[
    Widget(),
    Widget(),
    Widget(),
    Widget(),
  ], 
),

Column(
  children: <Widget>[
    Widget(),
    Widget(),
    Widget(),
    Widget(), 
   ],
),
```
Notice that they both have a children property which is an array of Widgets. All widgets in the children array will be displayed in the order you add them. You can even have rows inside columns and vice versa as many levels deep as you like.

Note Occasionally you’ll want two things above and below when the device is in landscape and side by side when in portrait. so you want them in a row at times and a column at others. this is when you’ll use a Flex widget which can do both. it has an orientation property that will be conditional:

```dart
Flex(
   direction:
     MediaQuery.of(context).orientation ==
     Orientation.landscape ?
        Axis.horizontal : Axis.vertical,
   children: <Widget>[
     SomeWidget(),
     SomeWidget(),
     SomeWidget(),
    ],
),
```
# The ListView widget

The easiest way to scroll is with a ListView.

ListView has actually has four different ways to use it:
1. new ListView – Normal use. It has a children property that takes a collection of static widgets.
2. ListView.builder – For dynamically creating children from a list of items.
3. ListView.separated – Like builder but also puts a widget between each item. Great for inserting ads in the list periodically.
4. ListView.custom – For rolling your own advanced listviews.


# Container widget and the box model

Flutter has the same concept **box mode**, the ideas of borders, padding, and margin.

Flutter doesn’t have a `<div>`, but it does have a div-like widget called
a Container which contains other things. In fact, its entire life purpose is to apply layout and styles to the things inside of it. An HTML `<div>` can hold multiple things, but a **Flutter Container only holds one child**. It has properties called padding, margin, and decoration.

Following is an example for displaying a picture from internet. Image widgets don't have a padding, margin, or borders. So you use Container to apply box model.
```dart
Container(
  padding: EdgeInsets.all(8.0),
  margin: EdgeInsets.all(10.0),
  decoration: BoxDecoration(border: Border.all(width: 1.0)),
  child:   Image.network(thePicture),
  // Container has *lots* of other properties
),
```

## Alignment and positioning within a Container
When you place a small child widget in a large Container, there will be more space in the Container than is needed by its child widget. That child widget will be located in the top-left corner by default. You have the option of positioning it with the alignment property:

```dart
Container(
  width: 150, height: 150,
  alignment: Alignment(1.0, -1.0),
  child:   Image.network(
    _peopleList[i]['picture']['thumbnail'],
  ),
),
```
Those alignment numbers represent the horizontal alignment (–1.0 is far left, 0.0 is center, and 1.0 is far right) and the vertical alignment (–1.0 is top, 0.0 is center, and 1.0 is bottom).

But you will probably prefer to use English words rather than numbers
when you can:

```dart
Container(
  width: 150, height: 150,
  alignment: Alignment.centerLeft,
  child:   Image.network(
    _peopleList[i]['picture']['thumbnail'],
  ),
),
```
Alignment can take on any of these values: topLeft, topCenter, topRight, centerLeft, center, centerRight, bottomLeft, bottomCenter, and bottomRight.

**Tip** the align widget is a shorthand for specifying the alignment and no other properties. the Center widget is merely a shorthand for centering.
```dart
Container(
 alignment:
  Alignment.center,
 child: Text("foo"),
),
Align(
alignment:
Alignment.center,
child: Text("foo"),
),
Center(
child: Text("foo"),
),
```
these three are equivalent.

# Special layout widgets

## Stack widget

This is for when you want to layer widgets so that they overlap one another. You want to stack them in the Z-direction. With Stack, you’ll list some number of widgets, and they’ll be displayed in that order one on top of another. The last one will occult (hide) the previous one if they overlap which will occult the one before that which will overlap the one before that and so on.

## GridView widget

Here’s another thing borrowed from HTML and the Web. GridView is for displaying a list of widgets when you want them to appear in rows and columns but don’t particularly care which rows and which columns – you just want them to show up in a grid.

To use a GridView, you’ll set its children property to the list of widgets you want to display and it will create the grid populating across and then wrapping to the next row, resizing its space available until it just fits. And here’s the greatest part, it automatically scrolls!
GridView has two constructors, GridView.extent() and GridView.count().
- Extent refers to the maximum width of the child. GridView will only let its kids grow to that size.
- With the `count()` constructor, you specify how many columns you want regardless of orientation. 

## The Table widget

The GridView is great when displaying widgets in rows and columns that wrap. The wrapping part means that you really don’t care what children widgets end up in which row and column.

Rows and Columns are best when you do care in which row and column the children exist. 

**Caution** anyone coming from an htML background knows that you can lay out a page using htML `<table>`s is possible but it is a bad idea. `<table>`s are for data, not for layout. Well it’s the same thing in Flutter. it is possible, but generally speaking, stay away from tables for laying out a page. But if you have data, tables are the right choice.


# Navigation and Routing 

All apps have the concept of moving from one screen to another. The user clicks the cart button, and we go to the card screen. The user clicks “continue shopping” button, and we get to browse for more products to buy. Some app developers call it routing. Others call it navigation. Whatever you want to call it, this is one area that Flutter makes really easy because there are only four ways of navigating:

- Stacks – Each widget is full screen. The user taps a button to go through a predefined workflow. History is maintained, and they can travel back one level by hitting a back button.
- Drawers – Most of the screen shows a widget, but on the left edge, a drawer is peeking out at the user. When they press it or swipe it right, it slides out revealing a menu of choices. Pressing one changes the widget in the main part of the screen.
- Tabs – Some room is reserved for a set of tabs at the top or the bottom of the screen. When you press on a tab, we show the widget that corresponds to that tab.
- Dialogs – While these aren’t technically part of navigation, they are a way to see another widget, so we’ll allow it. Dialogs are modal (aka pop-up windows) that stay until the user dismisses them.

Each of these methods depends on your app having a MaterialWidget as its ancestor.

## Stack Navigation

Flutter’s navigation works with stacks. When you want to send the user to a new scene, you will `push()` a widget on the top of the stack and the user sees that widget. Each time you `push()`, you’re making the stack of scenes taller and taller. When you are ready for them to go back to where they were before, you’ll `pop()` the last scene off the top of the stack, and what is revealed? The previous scene.

With Flutter’s stack, you’ll typically predefine the scenes (aka routes) and give each a name. This must be done at the MaterialApp level like so:

```dart
Widget build(BuildContext context) {
  return MaterialApp(
    title: 'Shopping App',
    initialRoute: '/',
    routes: {
      '/': (BuildContext ctx) => LandingScene(),
      '/browse': (BuildContext ctx) => Browse(),
      '/product': (BuildContext ctx) => ViewProduct(),
      '/checkout': (BuildContext ctx) => Checkout(),
    },
  ); 
}
```
**Note** that with routing, we no longer use the `home` property. Instead, use the `intialRoute` property.
**Tip** if your initialroute is “/”, you can omit it altogether and Flutter assumes it is “/”.

## Navigating forward and back
To navigate the user to a scene manually, you’ll `Navigator.pushNamed(context, route)` and `Navigator.pop(context)`.
To push a user to another route:
```dart
RaisedButton(
  child: const Text('Check out'),
  onPressed: () => Navigator.pushNamed(context, '/checkout),
),
```
Once they’re finished and want to go back:
```dart
RaisedButton(
  child: const Text('Go back'),
  onPressed: () => Navigator.pop(context),
),
```
But wait, there’s more! Notice that if you have a Scaffold, a back arrow is automatically added to the appbar. When tapped, it works to go back. And if your user is on Android, the ubiquitous Android back button works also.

**Tip** there is another flavor of routing that doesn’t use a predefined routing table in your Materialapp. instead, you generate the route on the fly:
```dart
Navigator.push<void>(context, MaterialPageRoute
<void>(builder: (BuildContext context) =>
SecondRoute());
```

### Get result after a scene is closed

With stack navigation, every `pop()` returns to its caller. Therefore, it is possible to return a value from each scene. 

We’d push() a little differently having a variable receive the returned value:
```dart
// The 'async' is needed here because we are 'await'ing below.
onPressed:  () async {
  _user.twitterHandle =
           await Navigator.pushNamed(context, '/twitter');
},
```
**Note** the `await` keyword implies that `pushNamed()` returns a `Future`. also note that any value returned from this route will be assigned to `_user.twitterhandle`.

So how does this value get returned? In the `pop()` of course!
```dart
Navigator.pop<String>(context, twitterHandle);
```
`Navigator.pop()` is overloaded. If you add a second parameter, it will be returned to the widget that called `push()` in the first place. In the preceding example, `twitterHandle` will be returned.

## Drawer navigation (hamberger menu)

Drawers are great when we have a lot of navigation choices – too many choices to fit in a tab.

You’ll need a Drawer widget, a built-in Flutter widget that has the ability to slide out, slide in, and contain menu choices. When you use a drawer, you always include it in a Scaffold’s drawer property, like this:
```dart
Widget build(BuildContext context) {
  return Scaffold(
    appBar: AppBar(
      title: const Text('Drawer Navigation'),
    ),
    body: const Text('DrawerNavigation'),
    drawer: Drawer(child: ListView(
      children: <Widget>[
        Text('Option 1'),
        Text('Option 2'),
        Text('Option 3'),
      ], 
    ),),
  ); 
}
```

**Tip** do you want a consistent drawer to be available across your entire app? if so, we generally put a Scaffold on every scene and include the drawer in it. therefore, it is best to put your drawer in its own widget and include it:
```dart
return Scaffold(
     appBar: AppBar(
       title: const Text('Drawer Navigation'),
     ),
   body: const Text('DrawerNavigation'),
   drawer: MyDrawer(),
 );
```

### Filling the drawer

Adding the drawer is easy. The trick is getting entries into the drawer and then making them navigate to another widget. Note that Drawer has a child property that accepts a single widget. To get multiple children in your drawer, you will use a widget that supports them such as Column (doesn’t scroll) or ListView (scrolls).

Whichever you choose, you’ll want to put something that is tappable because to navigate, you’re going to call `Navigator.push(`) or `Navigator.pushNamed()` just like you did with stack navigation.

**Tip** there’s a cool widget called a drawerheader that is built to take up a large area at the top of the drawer. it is great for putting your logo or other branding information to sort of remind the user what app they are in. it is cosmetic only but it really does look cool.
```dart
return Drawer(
  child: ListView(
    children: <Widget>[
      DrawerHeader(
        child: Stack(
          children: <Widget>[
            Image.asset(
              'lib/assets/images/BrandLogo.jpg',
            ),
            Container(
                alignment: Alignment.bottomRight,
                child: Text(
                  'My Brand',
                  style: Theme.of(context).textTheme.display1,
                )
            ),
          ], 
        ),
      ), 
      ListTile(
        leading: const Icon(Icons.looks_one),
        title: const Text('Widget 1'),
        onTap: () {
        Navigator.pushNamed(context, '/widget1');
        },
      ), 
      ListTile(
        leading: const Icon(Icons.looks_two),
        title: const Text('Widget 2'),
        onTap: () {
        Navigator.pushNamed(context, '/widget2');
        },
      ), 
      ListTile(
        leading: const Icon(Icons.looks_3),
        title: const Text('Widget 3'),
        onTap: () {
        Navigator.pushNamed(context, '/widget3');
        },
      ), 
    ],
  ), 
);
```

## Tab Navigation

As you would imagine, a tab system matches N tabs with N widgets. When the user presses tab 1, they see widget 1 and so forth. The matching is done with a `TabBar` widget, a `TabBarView` widget, and a `TabBarController`.

### TabController
The TabController is the least obvious part. Just know that you have to have one or you get the error.

When creating a TabBar, you must either provide an explicit TabController using the "controller" property, or you must ensure theat there is a DefaultTabController above the TabBar. 

### TabBarView
Next you’ll want to add a TabBarView widget. This holds the widgets that will eventually be shown when the user presses a tab, defining where they will be shown. Usually this is the entire rest of the screen, but you have the opportunity to put widgets above the TabBarView or below it or really anywhere around it:
```dart
child: Scaffold(
  body: TabBarView(
    children: <Widget>[
      WidgetA(),
      WidgetB(),
      WidgetC(),
  ], 
),
```

### TabBar and Tabs
Lastly we define the tabs themselves. Tabs can either hold text or an icon or both. Here’s a TabBar with three tabs, each having both an icon and text:
```dart
child: Scaffold(
  appBar: AppBar(
    title: const Text('Tab Navigating'),
    bottom: TabBar(
      tabs: const <Widget>[
        Tab(icon: Icon(Icons.looks_one), child:Text('Show A')), 
        Tab(icon: Icon(Icons.looks_two), child:Text('Show B')), 
        Tab(icon: Icon(Icons.looks_3), child: Text('Show C')),
      ]), 
...
```

**Caution** there’s a one-to-one correspondence between each tab and each tabBarview child; they are matched positionally. You must have the same number of tabs as you do widgets inside the tabBarview.

### TabBar at the bottom

The Scaffold has a property called bottomNavigationBar and it is built to hold a TabBar:
```dart
child: Scaffold(
  ...
  bottomNavigationBar: Material(
    color: Theme.of(context).colorScheme.primary,
    child: TabBar(tabs: const <Widget>[
      Tab(icon: Icon(Icons.looks_one), child: Text('Show A')),
      Tab(icon: Icon(Icons.looks_two), child: Text('Show B')),
      Tab(icon: Icon(Icons.looks_3), child: Text('Show C')),
    ]), 
  ),
),
```

**Note** the tabBar has the normal appearance of light text on a dark background. thus, when you place the tabBar on top of a light background, it may be difficult to see the text (light on light). to fix this, wrap your tabBar in a Material widget with a darker background color as we did earlier.

## The Dialog widget

### showDialog( ) and AlertDialog
showDialog() is a built-in Flutter method. You must supply a context and
a builder method that returns a Widget, usually either SimpleDialog or AlertDialog. The AlertDialog has an actions parameter – a List of (typically) FlatButtons that let the user dismiss the dialog.
```dart
RaisedButton(
  child: const Text('I am a button. Press me'),
  onPressed: () => showDialog<void>(
    context: context,
    builder: (BuildContext context) {
      return AlertDialog(
        content: const Text('Press OK to continue'),
        actions: <Widget>[
          FlatButton(
              child: const Text('OK'),
              onPressed: () => Navigator.pop(context)),
        ], 
      );
    }, 
  ),
),
```

### Responses with a Dialog

showDialog() returns a `Future<T>` which means that you can have it return a value to its caller. Let’s pretend you want the user to respond with yes or no.
```dart
RaisedButton(
  child: const Text('Get a response'),
  onPressed: () async {
    // The builder returns the user's choice here.
    // Since it is a Future<String>, we 'await' it to
    // convert it to a String
    String response = await showDialog<String>(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          content: const Text('Are you sure?'),
          actions: <Widget>[
            FlatButton(
              child: const Text('Yes'),
              // Return "Yes" when dismissed.
              onPressed: () => Navigator.pop(context, 'Yes')),
            FlatButton(
              child: const Text('No'),
              // Return "No" when dismissed.
              onPressed: () => Navigator.pop(context, 'No')),
          ], 
        );
      }, 
    );
    // Do things with the response that we 'await'ed above.
    print(response);
  },
),
```
**Tip** as the name suggests, the Simpledialog widget is a simpler version of the alertdialog. it doesn’t have actions and has fewer constructor parameters like titletextStyle, contenttextStyle, and the like. use it mainly if you don’t need the user to respond to the prompt but simply to inform.

# Managing State

## What is state?
State is widget data whose change requires a re-render.

StatelessWidgets might have data, but that data either doesn’t change or doesn’t change how the screen looks while the widget is alive. Sure, it may change when Flutter destroys and recreates the widget, but that doesn’t count. To be state, it must change while the widget is active, and that change requires a re-render in order to stay current.

## What goes in a StatefulWidget?

Here’s the shape of a StatefulWidget:
```dart
class Foo extends StatefulWidget {
  @override
  _FooState createState() => _FooState();
}
class _FooState extends State<Foo> {
  //Private variables here are considered the 'state'
  @override
  Widget build(BuildContext context) {
    return someWidget;
  }
}
```
We traditionally write stateful widget in one Dart file, but it always consists of two classes: the widget class and a state class.

The widget class inherits from StatefulWidget and is public because it is the thing that will be placed in other widgets.
The state class is always private because the current widget is the only thing that will ever see this class. The state class is responsible to ...
1. Define and maintain the state data.
2. Define the build() method – It knows how to draw the widget on screen.
3. Define any callback functions needed for data gathering or event handling.

## The most important rule about state!
When you change any state value, you should do it ...
1. In the state class
2. Inside a function call to setState():
```dart
setState(() {
    // Make all changes to state variables here...
    _value = 42; // <-- ... Like this
});
```

setState() not only sets the variables in the most efficient and controlled way, but it always forces a re-render of this widget to occur. It invokes build() behind the scenes. The end result: When you change a value, the widget redraws itself and your user sees the new version. Note that if this widget has subwidgets inside of it (aka inner widgets), they’ll be in the build() method, so a call to setState() actually redraws everything in this widget including all of its subtrees.


