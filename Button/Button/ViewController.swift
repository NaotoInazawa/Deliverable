//
//  ViewController.swift
//  Button
//
//  Created by Naoto Inazawa on 2021/09/16.
//

import UIKit

class ViewController: UIViewController {
    @IBOutlet weak var label: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

    @IBAction func frogbutton(_ sender: Any) {
        label.text = "げこげこ"
    }
    
    @IBAction func catbutton(_ sender: Any) {
        label.text = "にゃーにゃー"
    }
    
    @IBAction func dogbutton(_ sender: Any) {
        label.text = "わんわん"
    }
    
    
    
}

