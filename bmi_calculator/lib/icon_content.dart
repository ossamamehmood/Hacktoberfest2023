import 'package:flutter/material.dart';

class IconContent extends StatelessWidget {
  IconContent({@required this.iconText, @required this.iconIcon});

  final String iconText;
  final IconData iconIcon;
  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: <Widget>[
        Icon(
          iconIcon,
          size: 80.0,
        ),
        SizedBox(
          height: 15.0,
        ),
        Text(
          iconText,
          style: TextStyle(
            fontSize: 18.0,
            color: Color(0xff8d8e98),
          ),
        )
      ],
    );
  }
}
