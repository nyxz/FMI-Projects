<?xml version="1.0" encoding="UTF-8"?>
<tileset name="triggers" tilewidth="32" tileheight="32">
 <image source="triggers.png" width="256" height="128"/>
 <tile id="0">
  <properties>
   <property name="blockers" value="tr"/>
   <property name="top" value="yes"/>
   <property name="right" value="yes"/>
  </properties>
 </tile>
 <tile id="1">
  <properties>
   <property name="blockers" value="lr"/>
   <property name="right" value="yes"/>
   <property name="left" value="yes"/>
  </properties>
 </tile>
 <tile id="2">
  <properties>
   <property name="blockers" value="tlr"/>
   <property name="left" value="yes"/>
   <property name="right" value="yes"/>
   <property name="top" value="yes"/>
  </properties>
 </tile>
 <tile id="3">
  <properties>
   <property name="blockers" value="lrb"/>
   <property name="right" value="yes"/>
   <property name="left" value="yes"/>
   <property name="bottom" value="yes"/>
  </properties>
 </tile>
 <tile id="8">
  <properties>
   <property name="blockers" value="tl"/>
   <property name="top" value="yes"/>
   <property name="left" value="yes"/>
  </properties>
 </tile>
 <tile id="9">
  <properties>
   <property name="blockers" value="bl"/>
   <property name="bottom" value="yes"/>
   <property name="left" value="yes"/>
  </properties>
 </tile>
 <tile id="10">
  <properties>
   <property name="blockers" value="br"/>
   <property name="right" value="yes"/>
   <property name="bottom" value="yes"/>
  </properties>
 </tile>
 <tile id="11">
  <properties>
   <property name="blockers" value="tb"/>
   <property name="bottom" value="yes"/>
   <property name="top" value="yes"/>
  </properties>
 </tile>
 <tile id="16">
  <properties>
   <property name="blockers" value="t"/>
   <property name="top" value="yes"/>
  </properties>
 </tile>
 <tile id="17">
  <properties>
   <property name="blockers" value="l"/>
   <property name="left" value="yes"/>
  </properties>
 </tile>
 <tile id="18">
  <properties>
   <property name="blockers" value="r"/>
   <property name="right" value="yes"/>
  </properties>
 </tile>
 <tile id="19">
  <properties>
   <property name="blockers" value="b"/>
   <property name="bottom" value="yes"/>
  </properties>
 </tile>
 <tile id="20">
  <properties>
   <property name="blockers" value="trb"/>
   <property name="right" value="yes"/>
   <property name="top" value="yes"/>
   <property name="bottom" value="yes"/>
  </properties>
 </tile>
 <tile id="21">
  <properties>
   <property name="blockers" value="tlb"/>
   <property name="bottom" value="yes"/>
   <property name="left" value="yes"/>
  </properties>
 </tile>
 <tile id="25">
  <properties>
   <property name="blockers" value="tlrb"/>
   <property name="right" value="yes"/>
   <property name="top" value="yes"/>
   <property name="bottom" value="yes"/>
   <property name="left" value="yes"/>
  </properties>
 </tile>
 <tile id="26">
  <properties>
   <property name="player" value="yes"/>
  </properties>
 </tile>
 <tile id="27">
  <properties>
   <property name="enemy" value="yes"/>
  </properties>
 </tile>
 <tile id="28">
  <properties>
   <property name="exit" value="yes"/>
  </properties>
 </tile>
 <tile id="29">
  <properties>
   <property name="reverse" value="yes"/>
  </properties>
 </tile>
</tileset>
