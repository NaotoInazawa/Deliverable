//
//  ViewController.swift
//  BMIcalculator
//
//  Created by Naoto Inazawa on 2021/09/18.
//

import UIKit

class ViewController: UIViewController {
    @IBOutlet weak var heightfield: UITextField!
    @IBOutlet weak var weightfield: UITextField!
    @IBOutlet weak var BMIlabel: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        heightfield.placeholder = "身長を入力してください"
        weightfield.placeholder = "体重を入力してください"

    }

    @IBAction func calcbutton(_ sender: Any) {
        let doubleH = Double(heightfield.text!)
        let doubleW = Double(weightfield.text!)
        BMIlabel.text = calclation(height: doubleH!, weight: doubleW!)
        
    }
    
    func calclation(height: Double, weight: Double)-> String {
        let h = height / 100
        let w = weight
        var result = w / (h * h)
        result = floor(result * 10) / 10
        
        return result.description
    }
}

