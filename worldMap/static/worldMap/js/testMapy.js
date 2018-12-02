//alert("zaladowalo");
var cityListNamesq = [];
var cityListXq = [];
var cityListYq = [];
var cityListOwnerNamesq = [];
var game = new Phaser.Game(1155, 800, Phaser.CANVAS, 'worldMapDiv', { preload: preload, create: create, update: update, render: render });

function preload() {
    game.load.image('backgroundMap', backgroundMap); // ready
	game.load.image('cityIcon5', cityIcon5); // ready
	game.load.image('cityIcon4', cityIcon4); // ready
	game.load.image('cityIcon3', cityIcon3); // ready
	game.load.image('cityIcon2', cityIcon2); // ready
	game.load.image('cityIcon1', cityIcon1); // ready
	game.load.image('infoPanel', infoPanel); // ready
	game.load.atlasJSONHash('tankGif', tankGif, tankGif_rules); // ready
    cityListNamesq = cityListNames;
    cityListOwnerNamesq = cityListOwnerNames;
    cityListXq = cityListX;
    cityListYq = cityListY;

    liczbaMiast = cityListNamesq.length;
}

var cursors;
var x = 200;
var y = 200;
var pos_x = 450;
var pos_y = 450;
var city_list = [];
var cityListInfo = [];

var armyList = [];
var infoPanel;
var text;
var liczbaMiast = 0;
var lineList = [];




class cityInfoPanelClass{
	constructor(x, y, nazwaWioski, wlasciciel, punkty) {
		this.x = x;
		this.y = y;
		this.nazwaWioski = nazwaWioski;
		this.wlasciciel = wlasciciel;
		this.punkty = punkty;
		if(punkty > 3999){
			this.cityIcon = "cityIcon5";
		}
		if(punkty>2999 && punkty < 4000){
			this.cityIcon = "cityIcon4";
		}
		if(punkty>1999 && punkty < 3000){
			this.cityIcon = "cityIcon3";
		}
		if(punkty>999 && punkty < 2000){
			this.cityIcon = "cityIcon2";
		}
		if(punkty < 1000){
			this.cityIcon = "cityIcon1";
		}
		this.sprite = game.add.sprite(this.x, this.y, this.cityIcon);
	}
	sayHi() {
		alert(this.nazwaWioski);
	}
}

function create() {
    game.physics.startSystem(Phaser.Physics.ARCADE);

	game.world.setBounds(-0, -0, 3200, 2400);

	game.add.sprite(0, 0, 'backgroundMap');
	text = game.add.text(x+50, y, '', { font:"10px Arial", fill: 'black' });


	for(var i=0; i<liczbaMiast;i++){
		cityListInfo[i] = new cityInfoPanelClass(parseInt(cityListXq[i]), parseInt(cityListYq[i]), cityListNamesq[i], cityListOwnerNamesq[i], cityListPoints[i]);
		cityListInfo[i].sprite.events.onInputOver.add(listenerOverCity, this, 0, cityListInfo[i].x, cityListInfo[i].y, cityListInfo[i].nazwaWioski, cityListInfo[i].wlasciciel, cityListInfo[i].punkty);
		cityListInfo[i].sprite.events.onInputOut.add(listenerOverCityDelete);
		cityListInfo[i].sprite.events.onInputDown.add(listenerClickCity, this);
		cityListInfo[i].sprite.inputEnabled = true;
	}

	for(var i=0;i<liczbaArmi;i++){
        lineList[i] = new Phaser.Line(parseInt(cityListAttackerX[i])+25, parseInt(cityListAttackerY[i])+25, parseInt(cityListDefenderX[i])+25, parseInt(cityListDefenderY[i])+25);

        var graphics=game.add.graphics(0,0);
        graphics.lineStyle(10, 0xffd900, 1);
        graphics.moveTo(lineList[i].start.x,lineList[i].start.y);
        graphics.lineTo(lineList[i].end.x,lineList[i].end.y);
        graphics.endFill();

        armyList[i] = game.add.sprite(parseInt(cityListAttackerX[i]), parseInt(cityListAttackerY[i]), 'tankGif');

        game.time.events.add(Phaser.Timer.SECOND * 5, stopAnimation, this, armyList[i]);
        //armyList[i].events.onAnimationStart.add(stopAnimation, this, 0, i);

        armyList[i].animations.add('run');
        armyList[i].animations.play('run', 15, true);
        game.physics.arcade.enable(armyList[i]);

        game.physics.arcade.moveToXY(armyList[i], parseInt(cityListDefenderX[i]), parseInt(cityListDefenderY[i]), 10, 5000);

    }

    cursors = game.input.keyboard.createCursorKeys();

}

function stopAnimation(i) {
    i.destroy();
    //alert("One of your army arrived at destination");
}

function listenerClickCity() {

}

function listenerOverCity(one, two, xx, yy, nazwaWioski, wlasciciel, punkty) {
	infoPanel = game.add.sprite(xx+50, yy, 'infoPanel');
	text = game.add.text(xx+50, yy, '', { font:"10px Arial", fill: 'black' });
    text.text = "Nazwa wioski: " + nazwaWioski + "\nWlasciciel: " + wlasciciel + "\npunkty: " + punkty + "\npoz X: " + xx + "\npoz Y: " + yy;

}

function listenerOverCityDelete() {
    text.text="";
	infoPanel.destroy();
}

function update() {

    if (cursors.up.isDown)
    {
        game.camera.y -= 4;
    }
    else if (cursors.down.isDown)
    {
        game.camera.y += 4;
    }

    if (cursors.left.isDown)
    {
        game.camera.x -= 4;
    }
    else if (cursors.right.isDown)
    {
        game.camera.x += 4;
    }

}

function render() {

}
