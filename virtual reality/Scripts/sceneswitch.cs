using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class sceneswitch : MonoBehaviour
{
 private float timer=10f;
 private Text timerseconds;

 void start (){
  timerseconds=GetComponent<Text>();

 }

 void update(){
  timer-=Time.deltaTime;
  timerseconds.text=timer.ToString("f0");
  if(timer<=0){
    SceneManager.LoadScene(1);
  } }

   
}
