using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class RotationScript : MonoBehaviour
{
public Slider slider;
    public Transform StartAxis;
    public Transform Lose;
    public Transform Win;

    private void Start()
    {
        transform.localRotation = StartAxis.localRotation;
    }

    private void Update()
    {
        float t = slider.value / slider.maxValue;
        Quaternion targetRotation = Quaternion.Lerp(Lose.localRotation, Win.localRotation, t);
        if(slider.value  >= slider.maxValue / 2)
            transform.rotation = Quaternion.Lerp(StartAxis.localRotation, targetRotation, t);
        else
            transform.rotation = Quaternion.Lerp(targetRotation , StartAxis.localRotation, t);
    }
}
