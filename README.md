
常用的odoo相关模块

|Author|果冻虾仁|
|---|---
|- A dict (text input step). The key 'default' is the default value, the key 'size' is the maximum size before automatic validation.|
|- A dict of strings (list step). The key is the returned value, the second value is the displayed value.|
|- A list of strings (all step types). Each string corresponds to a line of text to display. The long lines will be splitted automatically to fit on screen.|
|- A list of tuples of two strings (list steps). The first value of each tuple is the returned value, the second value is the displayed value.|
|- A single value (all step types). The type of the value depends on the type of step (float, integer, boolean...).|
|- act : Type of step|
| lot '%s'|
| On Hand|
|- res : Content to display|
|- val : Default value|
|        Allows to get product availability taking into account lot removal date        |
|        Allows to restrict location to a dedicated procurement group        (e.g. : For orders waiting delivery)|
|        Compute stock cost as following logic:    |
|        Makes destination package mandatory on stock pack operations|
|        Purchase cost, sales cost, stock cost|
|        Reimplement barcode field in Product Packagings|
|        Stock pack operation auto fill|
|        Stock Quantity Change Reason |
|        This module allows to fill in a date in the standard wizard that        changes product price. That helps accountant to add some product        past values|
|Presentation:The module Barcode_link adds a field Link in the barcode form.And link the barcode with a product.|
|Presentation:This module add a wizard to fill in packaging.This wizard is used to add or remove an object from a package.Adding to the historical movements and parent objects|
|Presentation:This module adds a field into the product category to define if this should be tracked or not.|
|Presentation:This module adds a sequence for generating automatically inventories name|
|Presentation:This module adds some info into packs to get a better tracking of products and serial lots inside of these packs|
|Presentation:This module adds the packaging into the production lot|
|Presentation:This module allows to define and identify package in parent or child|
|Presentation:This module allows to define and identify package in parent or child|
|Presentation:This module allows to move all stock in a stock location to an other one.And adds fields and buttons to advance in Physical Inventories.|
|Presentation:This module allows to move packing with a wizardand adds fields for source location and destination location in History.|
|Presentation:This module Change reference of the packaging if it's re-open.|
|Presentation:This module will add the state field to make changes of closed packed|
|Account Dashboard|
|Account Payment Report|
|Account Period|
|Account Period|
|Account Voucher|
|Add a wizard to configure massively order points for multiple product|
|Adds the possibility to specify the origin country of goods and the partner VAT in the Intrastat XML report.    |
|Extends orderpoint wizard to configure massivelystock location flows for multiple product|
|Multiple EAN13 on products==========================Allow Multiple EAN13 on products.A list of EAN13 is available for each product with a priority, so amain ean13 code is defined.|
|Replaces the legacy rml picking Order report by brand new webkit reports.Three reports are provided: - Aggregated pickings - Aggregated deliveries - Delivery Slip    |
|You can choose which stock moves have to generate inventory valuationaccounting entries, by specifying it in the location form.|
|%(user_name)s invited you to follow %(document)s document: %(title)s|
|%(user_name)s invited you to follow a new document|
|(No description provided.)|
|(Youtube, Vimeo, Dailymotion)|
| Login %s|
|Confirm step|
|Error step|
|Final step|
|Introduction|
|Message step|
|Number (integer) step|
|Quantity (float) step|
|Text input step|
|<p>Managers can validate or refuse expense reports.</p><p>If you refuse a report, explain the reason using the <i>New Message</i> button in the bottom.</p>|
|<p>Once completed, you can <b>submit the expense</b> for approval.</p><p><i>Tip: from the list view, select all expenses to submit them all at once, in a single report.</i></p>|
|<span class="o_stat_text">Expired Outgoing</span>|
|<span class="o_stat_text">Expired Outgoing</span>|
|<span class="o_stat_text">Expired</span>|
|<span class="o_stat_text">Expired</span>|
|<span><strong>Location address:</strong></span>|
|<span>Location:</span>|
|<strong>Complete name:</strong>|
|<strong>Current Accuracy:</strong>|
|<strong>Discount</strong>|
|<strong>Expected qty</strong>|
|<strong>Expiry date</strong>|
|<strong>Removal Date</strong>|
|<strong>Source document</strong>|
|A backorder was created : %s|
|A step designed to display some information, without waiting for any user input.|
|A001|
|A4|
|Acceptable Inventory Quantity Variance Threshold|
|Account Dashboard|
|Account Hierarchy|
|Account move ids|
|Account move ids|
|Account move line ids|
|Account move line ids|
|Account Move Line Product|
|Account Move Line Stock Move|
|Account Period|
|Account Period|
|Account Voucher|
|Accounting Value|
|Accounting Value|
|Accounting Value|
|Accuracy|
|Accuracy|
|Accuracy report|
|Accuracy Stats|
|Accuracy Stats|
|Action not allowed. Chained move.|
|Action not allowed. Move splited / with returned moves.|
|Action pack op auto fill allowed|
|Actual destination location|
|Actual Movement Date|
|Actual Movement Date|
|Add a MTS+MTO route|
|add filters on stock.picking views        |
|Add note, modification date, etc.|
|Add product depreciation|
|Add relation between assets and equipments|
|Add surface units of measure|
|Adding Triple Discount on Valued Picking Report|
|Adding Valued Picking on Delivery Slip report|
|Adds an internal carrier to delivery options|
|Adds fields uos and uos_quantity to Stock Transfer Details|
|Adds link between pickings and invoices|
|Adds report for stock picking in partner language|
|Adds the capability to request a Slot Verification when a inventory is Pending to Approve|
|Adds the capability to schedule cycle counts in a warehouse through different rules defined by the user.|
|Adds the capability to show the discrepancy of every line in an inventory and to block the inventory validation when the discrepancy is over a user defined threshold.|
|Adjust Stock Valuation Account Discrepancies|
|Adjustment amount|
|Adjusts valuation of the products and quants when the cost method or type of a product changes|
|administrator|
|administrator|
|After this step, the scenario automatically goes back if the returned value is set to True.|
|After this step, the scenario is finished.|
|All Content|
|All step types allow the user to scroll if the text doesn't fit on screen.|
|All steps must return three values :|
|All stock moves have been cancelled for this procurement.|
|All the transfers must be "Ready to Transfer".|
|All the transfers must have the same destination location|
|Allow negative stock levels for the stockable products attached to this category. The options doesn't apply to products attached to sub-categories of this category.|
|Allow to define an other user for execute all scenarios with that scanner instead of default user.|
|Allow to force availability on stock operations|
|Allow to perform inventories of a location without including its child locations.|
|Allowed Groups|
|Allowed Users|
|Allowed Users|
|Allowed Users Groups|
|Allows managing barcode readers with simple scenarios|
|Allows to configure the system to propose automatically new procurement groups in procurement orders.|
|Allows to create demand estimates.|
|Allows to create procurement orders from orderpoints instead of relying only on the scheduler.|
|Allows to create procurement orders in the UoM indicated in the orderpoint|
|Allows to set a stock level composed by a configuration using the sum of stock location + product fields|
|Allows to share the custom values with a shared scanner in the same warehouse.|
|An accounting period typically is a month or a quarter. It            usually corresponds to the periods of the tax declaration.|
|An error occuredPlease contact your administrator|
|An inventory is being conducted at the following location(s):%s|
|An inventory is being conducted at this location|
|An inventory is being conducted at this location|
|An unbuild order will do a reverse bill of materials, unbuilding products            you produced, but you can also use it to unbuild products you purchased.|
|Appear on barcode reader screen.|
|Applied in:|
|Apply this rule in:|
|Are you sure to want to finish this inventory ?|
|Are you sure you want to reopen this picking?|
|Are you sure you want to split current picking ?|
|Assigned to me|
|At least one reordering rule for this product has a different Procurement unit of measure category.|
|Auto fill operations|
|Auto-assignation of lots on pickings|
|Autoconfiguration failed !
Please enter terminal code|
|Automatic Move Processing|
|Available per stock|
|Available per stock|
|Avoid auto-assignment of lots|
|Back to draft|
|Back to Draft|
|Backorder strategy|
|Bank Statements Report|
|Bank Statements Report Wizard|
|Bank Statements Report Wizard|
|Barcode link Module|
|Barcodes - EAN14|
|Base - Background Color|
|Base - Text Color|
|Base Products Merge|
|Belgian Intrastat Declaration - Complement for 2019|
|Block stock entrance|
|By pressing the escape key, you can return back to the last 'Return step'.|
|Bye !|
|Can contain scenarios or submenus|
|Cannot cancel a done package preparation.|
|Cannot cancel a picking with multiple operations|
|Cannot do an inventory value change if the quantity available for product %s is 0 or negative|
|Cannot do an inventory value change if the quantity available for product %s is 0 or negative|
|Cannot find a default location for picking type: %s|
|Can't find any generic MTS+MTO route.|
|Can't find MTO Rule on the warehouse|
|Can't find MTS Rule on the warehouse|
|Capture Lines|
|Capture Lines|
|Carrier Pickup Picking|
|Cash Delivery From Carrier Picking|
|Cash on delivery|
|Cash Picking From Buyer Picking|
|cf_licensing|
|cfprint|
|CFSoft Receipt Manager|
|Change All|
|Change Cumulative Occurrence Wizard|
|Change Location|
|Change location of all picking operations|
|Change Operation Destination Location|
|Change quantity in manual procurements from reordering rules|
|Char Value 1|
|Char Value 2|
|Char Value 3|
|Char Value 4|
|Char Value 5|
|Check Availability after Inventories|
|Check expired lots|
|Check expired lots|
|Check expired lots|
|Check if you want change all operations without filter by old location|
|Check this box|
|check this box if you want to check the availability of the selected Pickings.|
|check this box if you want to force the availability of the selected Pickings.|
|check this box if you want to mark as Todo the selected Pickings.|
|check this box if you want to transfer all the selected pickings. You'll not have the possibility to realize a partial transfer. If you want  to do that, please do it manually on the picking form.|
|Check this for automatic orderpoints|
|Check this if this is the  last step of the scenario.|
|Check this if this is the first step of the scenario.|
|Check this if you want to compute stock level minus expired product lots (based on removal date) if it is defined|
|Check this if you want to restrict transfers to one procurement group only|
|Check this to prevent returning back this step.|
|Check this to stop at this step when returning back.|
|Choose between MTS and MTO|
|Click to add a fiscal period.|
|Click to create a stock reservation.|
|Click to prepare a new package preparation.|
|Click to start a new fiscal year.|
|Click to start a new Stock Inventory Revaluation.|
|Click to start a new Stock Valuation Account Manual Adjustment|
|Click to try <b>submitting an expense by email</b>. You can attach a photo of the receipt to the mail.|
|Client Error|
|Client order reference|
|Code of this hardware.|
|Color for the error background.|
|Color for the error text.|
|Color for the info background.|
|Color for the info text.|
|Common Dialog|
|Company to be used on this scenario.|
|Compute Cycle Count Rules|
|Configuration of order point in mass|
|Configure finance|
|Configure scanner module|
|Confirm Cycle Counts|
|Consider the production potential is available to promise|
|Costs types|
|Counts per period|
|Create both Supplier and Customer Invoices from a Dropshipping Delivery|
|Create configuration of stock location flow|
|Create Orderpoint|
|Create Orderpoint|
|Create Orderpoint|
|Create Orderpoints|
|Create Orderpoints|
|Created Procurements|
|Credit/Debit amount|
|Current Cost|
|Current cost|
|Current Step|
|Current step for this hardware.|
|Current Steps History|
|Customer Refund|
|Customers Deliveries|
|Cyan|
|Cycle Count|
|Cycle Count|
|Cycle Count|
|Cycle Count|
|Cycle Count #|
|Cycle Count Accuracy|
|Cycle Count Planning Horizon (in days)|
|Cycle Count planning horizon in days. Only the counts inside the horizon will be created.|
|Cycle count rule|
|Cycle Count Rules|
|Cycle Count Rules|
|Cycle count rules|
|Cycle Count Rules                    applied in this Warehouse:|
|Cycle Counting|
|Cycle Counts|
|Cycle Counts Assigned to me|
|Cycle Counts Cancelled|
|Cycle Counts Done|
|Cycle Counts in Execution|
|Cycle Counts Planned|
|cycle counts test:|
|cycle counts test:|
|Date and time of the last call to the system done by the scanner.|
|Date of actual processing|
|Date of actual processing|
|Deadline Date|
|Decoding API for GS1-128 (aka UCC/EAN-128) and GS1-Datamatrix|
|Decrease Account|
|Default color for the background.|
|Default color for the text.|
|Default orderpoint Max. product quantity|
|Default orderpoint Max. product quantity|
|Default Picking Type used in package preparation|
|Default Picking Type used in package preparation|
|Define the Financial Accounts to be used as the balancing account in the transaction created by the revaluation. The Valuation Decrease Account is used when the inventory value is decreased.|
|Define the G/L accounts to be used as the balancing account in the transaction created by the revaluation. The Decrease Account is used when the inventory value is decreased.|
|Define the G/L accounts to be used as the balancing account in the transaction created by the revaluation. The Increase Account is used when the inventory value is increased due to the revaluation.|
|Define what to do with backorder|
|Define whether the location is going to be cycle counted.|
|Define whether this location will trigger a zero-confirmation validation when a rule for its warehouse is defined to perform zero-confirmations.|
|Defines if this scenario is a menu or an executable scenario.|
|Deliveries Tracking|
|Delivery Company|
|Delivery Money Picking Type|
|Delivery Orders Mass Assign|
|Delivery Stock Picking Type|
|Destination package mandatory|
|Directly launch a scenario|
|Disable force availability button|
|Disable Zero Confirmations|
|Disallow negative stock levels by default|
|Discrepancy|
|Discrepancy percent (%)|
|Displays by default Inventory Revaluation. This text is copied to the journal entry.|
|Displays the current cost of the product.|
|Displays the current value of the product.|
|Displays the current value of the product.|
|Displays the previous cost of the product.|
|Displays the product in the journal entries and items|
|Do you really want to logout?|
|Do you really want to terminate this receipt?|
|Document Date|
|Docx|
|Docx|
|Don't use 'Removal Priority' in Locations|
|Edit Workflow|
|Empty list|
|Enable logging messages from scenarios.|
|Enforce ownership on stock availability|
|Enhance Serial Number management|
|Ensures that at least a defined number of counts in a given period will be run.|
|Enter a location's area based on different units of measure|
|Enter the amount you wish to credit or debit from the current inventory value of the item. Enter credit as a negative value.Relevant only if the selected revaluation type is Inventory Credit/Debit.|
|Enter the new cost you wish to assign to the product. Relevant only when the selected revaluation type is Price Change.|
|Enter the new cost you wish to assign to the Quant. Relevant only when the selected revaluation type is Price Change.|
|Enter the python code here|
|Enter the python code here|
|Error - Background Color|
|Error - Text Color|
|Error ! You can not create recursive scenarios.|
|Error ! You can not create recursive scenarios.|
|Error found determining the frequency of periodic cycle count rule. %s|
|Error found when comparing turnover with the rule threshold. %s|
|Error in condition for transition ""%s"" at line %d, offset %d:%s|
|Error in python code for step ""%s"" at line %d, offset %d:%s|
|Error: The product default Unit of Measure and the procurement Unit of Measure must be in the same category.|
|Establish a removal priority on stock locations.|
|Excel报表模板|
|Except the list steps, the user can scroll using the up/down arrow keys.|
|Exclude from Cycle Count|
|Exclude Sublocations|
|Execute|
|Expected Quantity|
|Expired Outgoing|
|Expired Outgoing|
|Expired Outgoing|
|Expired:|
|Expirity date|
|Extended Inventory Preparation Filters|
|extension of 'stock_quant_merge', and adds the cost as a criteria to merge quants.|
|Faster packaging process in Odoo|
|Faster packaging process with logistical units|
|Fill Actual Movement Date|
|Fill Actual Movement Date|
|Fill Actual Movement Date|
|Fill Actual Movement Date of all operations|
|Filling the operations automatically is not possible, perhaps the pickings aren't in the right state (Partially available or available).|
|Filter location id|
|finance_account_type_form|
|finance_account_type_form|
|finance_account_type_tree|
|finance_account_type_tree|
|Fixed per product location|
|Float Value 1|
|Float Value 2|
|Float Value 3|
|Float Value 4|
|Float Value 5|
|Force Availability|
|Force Availability|
|Force Validation|
|Forecast On Location|
|Generate Barcodes (Abstract)|
|Generate Barcodes for Any Models|
|Generate Barcodes for Packaging|
|Generate Barcodes for Partners|
|Generate Barcodes for Partners|
|Generate Barcodes for Product Packaging|
|Generate Barcodes for Products|
|Generate Barcodes for Products (Templates and Variants)|
|Generate Barcodes for Stock Locations|
|Generate Barcodes for Stock Pickings|
|Generate Barcodes for Stock Production Lots|
|Get Order Lines|
|Get Quants|
|Get Quants|
|Get Quants|
|Get Quants for Inventory Revaluation|
|Glue module for stock_orderpoint_uom and stock_orderpoint_manual_procurement|
|Go to Error step|
|Go to next step|
|Going back|
|Group Restricted|
|Hardware|
|Hardware linked to this history line.|
|Height of the terminal's screen.|
|Hello,|
|History of all steps executed by this hardware during the current scenario.|
|hr.expense.config.settings|
|ID of the model source.|
|ID of the reference document.|
|If check, this object is always available.|
|if this box is checked, putting stock on this location won't be allowed. Usually used for a virtual location that has childrens.|
|If this new route is selected on product form view, a purchase order will be created only if the virtual stock is less than 0 else, the product will be taken from stocks|
|If this option is selected, the move will be automatically processed as soon as the products are available.|
|If this option is selected, the move will be automatically processed as soon as the products are available.|
|If you change this quantity for a 'ready' picking, the system will not generate a back order, but will just deliver the new quantity|
|Ignore planned receptions in quantity available to promise|
|Impossible to create confirmed picking. Please Check products availability!|
|Impossible to create confirmed picking. Please Check products availability!|
|Improved reordering rules|
|In either case you can exclude specific locations                        going to the locations form and checking the box                        ""Exclude from Cycle Count"".|
|In order to close a fiscalyear, you must first post related journal entries.|
|In order to close a period, you must first post related journal entries.|
|In Pack|
|In picking out lots' selection, filter lots based on their location|
|In purchase, use package|
|In sale, use uom's package|
|In the stock transfer wizard, you can split by multiple units|
|In the update wizard of quantities for a product, sort the stock location by quantity|
|Inbound Buyer Picking|
|Incoming On Location|
|Incoming transitions|
|Incoming transitions|
|Incoming transitions|
|Incorrect model.|
|Increase Account|
|Info - Background Color|
|Info - Text Color|
|Int Value 1|
|Int Value 2|
|Int Value 3|
|Int Value 4|
|Int Value 5|
|Internal Unreserved|
|Introduces inventory revaluation as single point to change the valuation of products.|
|Introduction|
|Inv. Adj. Lines Involved|
|Invalid Action!|
|Invalid Action!|
|Invalid quantity %g!|
|Inventories for location accuracy calculation|
|Inventory Accuracy|
|Inventory Accuracy|
|Inventory accuracy evolution|
|Inventory adj count|
|Inventory Adjustment Line|
|Inventory Adjustment Lines related to the given location and product.|
|Inventory adjustments associated|
|Inventory Canceled|
|Inventory Confirmed|
|Inventory Control|
|Inventory Debit/Credit|
|Inventory Done|
|Inventory done !|
|Inventory Lock Down|
|Inventory Revaluation|
|Inventory revaluation|
|Inventory Revaluation|
|Inventory revaluation get Quants|
|Inventory revaluation quant|
|Inventory Valuation Manual Adjustments|
|Inventory Valuation Manual Adjustments|
|Inventory, Logistic, Storage|
|Involved inv line count|
|Involved Inventory Lines|
|Involved move count|
|Involved Stock Moves|
|ir_sequence_autoreset|
|Is Balance|
|is finished|
|is finished|
|Is Init Period|
|It provides an EAN14 barcode nomenclature.|
|Kit (Phantom): When processing a sales order for this product, the delivery order will contain the raw materials, instead of the finished product.|
|Last call|
|List Scrolling|
|List step|
|Location ?|
|Location ?|
|Location ids|
|Lock down stock locations during inventories.|
|Log changes being done in Inventory Adjustments|
|Log enabled|
|Login ?|
|Login/logout scenarii enabled|
|Logout cancelled|
|Long texts in a list allows the user to scroll horizontally with left/right arrow keys|
|Lot : %s|
|Lot ?|
|Lot Valuation|
|Lots effectively linked to stock move|
|Make Procurements from Orderpoint Item|
|Make Procurements from Orderpoint Item|
|Make Procurements from Orderpoints|
|Make Procurements from Orderpoints|
|Make To Order + Make To Stock|
|Manage origin / destination / consignee addresses on pickings|
|Manage origin / destination / consignee addresses on purchase requisitions|
|Manage origin / destination / consignee addresses on purchases|
|Manage origin / destination / consignee addresses on sales|
|Manages the order of stock moves by displaying its sequence|
|Manual quants|
|Manual Quants|
|Manual Quants|
|Mark as Cancelled|
|Mark as Solved|
|Mark as todo this picking please.|
|Mass Action for the selected stock picking|
|Mass Adjust Stock Valuation Account Discrepancies|
|Max sequence in lines|
|Max. product quantity|
|Maximum Discrepancy Rate allowed for any product when doing an Inventory Adjustment. Threshold defined in involved Location has preference.|
|Maximum Discrepancy Rate allowed for any product when doing an Inventory Adjustment. Thresholds defined in Locations have preference over Warehouse's ones.|
|Maximum Discrepancy Rate Threshold|
|Maximum Discrepancy Rate Threshold|
|Maximum Discrepancy Rate Threshold|
|Message sent during execution of the step.|
|Messages can be configured to appear during any operation: receptions, delivery orders,                manufacturing orders, work orders, etc.|
|Min. product quantity|
|Minimum Accuracy|
|Minimum Accuracy Threshold|
|Model used for these data.|
|Model used for this scenario.|
|Money Order Lines|
|Money Transfer Order Lines|
|More filters for inventory adjustments|
|Most common exceptions are products to purchase without                having a vendor defined on the product, and products to                manufacture without having a bill of materials.|
|Move ids|
|Move Stock Location|
|Move Stock Packaging|
|Moved lots|
|Moves are reserved.|
|Mto+Mts Procurement|
|MTO+MTS rule|
|MTS Rule|
|MTS+MTO|
|Multiple EAN13 on products|
|Name of the hardware.|
|Name of the step.|
|Name of the transition.|
|New Cost|
|New cost|
|New destination location|
|No back|
|No create|
|No create|
|No Expense account found for the product %s (or for it's category), please configure one.|
|No scenario available !|
|No transfer selected for this preparation.|
|No value available|
|Not Allowed, picking has backorder.|
|Not already reserved|
|not found|
|Number of Discrepancies Over Threshold|
|Number of latest inventories used to calculate location accuracy|
|oecharts|
|Old cost|
|Old destination location|
|Old value|
|Only canceled package preparations can be reset to draft.|
|Open Inventory Adjustment Lines|
|Opening Period|
|Orderpoint product quantity cannot be negative|
|osbzr|
|Outgoing On Location|
|Outgoing transitions|
|Outgoing transitions|
|Outgoing transitions|
|Output Type|
|Owner Lot Visibility|
|Pack operation ids|
|Package done|
|Package Preparation|
|Package Preparation|
|Package Preparation|
|Package Preparation|
|Package Preparation|
|Package Preparation Line|
|Package Preparations|
|Package Preparations|
|Package Preparations|
|Packaging UOM|
|Parent scenario, used to create menus.|
|Partner Location Auto Create|
|Partner Statements Report Wizard|
|Partner Statements Report Wizard|
|Pay Order Lines|
|Pending to Approve|
|Perform an Inventory Adjustment every time a location in the warehouse runs out of stock in order to confirm it is truly empty.|
|Period in days|
|period type|
|Periodic|
|Perpetual Inventory Valuation|
|Perpetual Inventory Valuation|
|Picking %s has invoices|
|Picking backordering strategies|
|Picking Dispatch Wave|
|Picking Priority|
|Picking reports using Webkit Library|
|Picking wave associated to this picking|
|Pickings back to draft|
|Pickup Name|
|Please add an Increase Account and a Decrease Account.|
|Please add Stock Valuation Account in Product Category|
|Please contact|
|Please contact|
|PLM|
|Post Inventory Revaluation|
|Post multiple inventory revaluations|
|Posting Date|
|Posting Date|
|Prepared|
|Presentation:This module add a wizard to fill in packaging.This wizard is used to add or remove an object from a package.Adding to the historical movements and parent objects|
|Presentation:This module add a wizard to swap packs in packaging.This wizard is used to replace an object from a package.Adding to the historical movements and parent objects|
|Presentation:This module add a wizard to swap products or prodlots in packaging.This wizard is used to replace an object from a package.Adding to the historical movements and parent objects|
|Preserve Ownership of moves (not pickings) on reception.|
|Prevent to add stock on flagged locations|
|Previous cost|
|Price Change|
|Process|
|Procure Recommendation|
|Procurement Auto Create Group|
|Procurement UoM|
|Product %s must have real time valuation|
|Product : %s|
|Product : %s|
|Product : %s|
|Product : [%s] %s|
|Product : [%s] %s|
|Product code ?|
|Product Expiry Available|
|Product Expiry Simple|
|Product Inventory Valuation|
|Product Packaging Barcode|
|Product putaway stragegy|
|Product Serial|
|Product stock locations|
|Product stock locations|
|Product stock locations|
|Product Supplierinfo For Customer Picking|
|Product UoM|
|Products you scrap will be removed from the stock and moved to a specific scrap location, for reporting purposes.|
|Provides a new field on stock pickings, allowing to display the corresponding backorders.|
|Purchase - Transport Addresses|
|Purchase Packaging|
|Purchase Requisition - Transport Addresses|
|Put Away Locations|
|Putaway strategy per product|
|Pwd ?|
|Python code to execute.|
|Qty Available Not Reserved|
|Qty Available Not Reserved|
|Qty in reservation UoM|
|Quantity : %g %s|
|Quantity : %g %s|
|Quantity : %g %s|
|Quantity done in UOM ordered|
|Quantity done store|
|Quantity expressed in the unit of measure of the move|
|Quantity is higher than the needed one|
|Quantity must be positive.|
|Quantity of products that are planned to leave but which should be removed from the stock since these are expired.|
|Quantity of products that are planned to leave but which should be removed from the stock since these are expired.|
|Quantity of products that are planned to leave but which should be removed from the stock since these are expired.|
|Quantity of stock available for immediate use|
|Quantity On Hand Unreserved|
|Quantity On Location|
|Quantity On Location (Unreserved)|
|Quotations in quantity available to promise|
|Quoted|
|Quoted|
|Quoted|
|Receipt done.|
|Receipt to treat ?|
|Recommended Request Date|
|Reconcile Inventory Account|
|Reconcile Order|
|Reconcile Order|
|record: browse_record of the record on which the action is triggered|
|Reference for the journal entry|
|Reference for the journal entry|
|Related order line|
|Related Pickings|
|Related Pickings|
|Related pickings (only when the invoice has been generated from a sale order).|
|Related pickings (only when the invoice has been generated from a sale order).|
|Related Stock Moves|
|Related stock moves (only when the invoice has been generated from a sale order).|
|Release|
|Release|
|Released|
|Remarks|
|Remarks|
|Remarks|
|Removal Priority|
|Removal Priority|
|Removal Priority|
|Removal Priority|
|Removal priority that applies when the incoming dates are equal in both locations.|
|Reopen cancelled pickings|
|Reordering rule|
|Request For Pickup|
|Request For Pickup|
|Request For Pickup|
|Request Procurement|
|Request Verification|
|Requested Verification?|
|Requests For Pickup|
|Required Date|
|Required Date|
|Reservation Move|
|Reservation Move|
|Reservation Stock|
|Reservation UoM|
|Reservations have been released.|
|Reserved qty|
|Reset Scenario|
|Responsible Company|
|Restricted|
|Restricted|
|Restricted|
|Restricted|
|Restricted|
|Restricted group|
|Restricted Group|
|Restricted Procurement Group Locations|
|Return values of a step|
|Returned pickings|
|Returns|
|Revaluation|
|Revaluation %s is not in Draft state|
|Revaluation line quants|
|Revaluation Type|
|Rule Description|
|Sale - Transport Addresses|
|Sale discount (%)|
|Sale Packaging|
|Sale price unit|
|Sale Reference/Description|
|Save the report, your manager will receive a notification by email to approve it.|
|Scanner|
|Scanner Configuration|
|Scanner Hardware|
|Scanner Hardware|
|Scanner Hardware|
|Scanner Hardware|
|Scanner Hardware|
|Scanner Scenario|
|Scanner Scenario|
|Scanner Scenario|
|Scanner Scenario|
|Scanner Scenario|
|Scanner status|
|scenario|
|Scenario|
|Scenario|
|Scenario|
|Scenario|
|Scenario|
|Scenario|
|Scenario|
|Scenario Custom Values|
|Scenario Custom Values|
|Scenario Custom Values|
|Scenario Custom Values|
|Scenario Editor|
|Scenario for scanner|
|Scenario for this step.|
|Scenario for this step.|
|Scenario Step|
|Scenario Step|
|Scenario Step|
|Scenario Step|
|Scenario Step|
|Scenario Step|
|Scenario used for this hardware.|
|Scenarios|
|Schedules a count every time the accuracy of a location goes under a given threshold.|
|Schedules a count every time the total turnover of a location exceeds the threshold. This considers every product going into/out of the location|
|Scrap expired lots|
|Scrap Production Lot|
|Screen colors|
|Screen Height|
|Screen size|
|Screen Width|
|Scrolling|
|Search Cycle Count|
|Search operator %s not implemented for value %s|
|Search operator %s not implemented for value %s|
|Search operator %s not implemented for value %s|
|Search Scrap Expired|
|Search Stock Inventory Revaluation|
|Search Voucher|
|Select quantity|
|Selected : %d|
|Selected : %s|
|Selected Categories|
|Selected Location Zones.|
|Selected Lots|
|Selected Products|
|Selected warehouses|
|Sentinel: technical users|
|Sequence order.|
|Sequence order.|
|Session validity in seconds|
|Set a product location and put-away strategy per product|
|Shared Custom|
|Shipment Date|
|Shipment Management (Consignment)|
|Shipped to|
|Shipping Date|
|Show lots on the partners that own them|
|Show returns on stock pickings|
|Shows in the product inventory stock value and the accounting value and allows to reconcile them|
|Shows the previous cost of the quant|
|Shows the sequence in the Stock Move.|
|Shows the sequence in the Stock Move.|
|Simpler and better alternative to the official product_expiry module|
|Slot Verification Request|
|Slot Verification Request|
|Slot Verification Request|
|Slot Verification Request|
|Slot Verification Requests|
|Slot Verification Requests|
|SO related filters on stock.picking and sale.order|
|Solved|
|Some Operations do not contain destinationpackages|
|Source Order Lines|
|Source Picking|
|Split a picking in two not transferred pickings|
|Split picking|
|Step back|
|Step executed during this history line.|
|Step for scenario|
|Step of the current running scenario.|
|Step start|
|Step stop|
|Step which is reached by this transition.|
|Step which launches this transition.|
|Steps|
|Steps History|
|Steps History of Scanner Hardware|
|Stock - Manual Quant Assignment|
|Stock - Quant merge|
|Stock - Transport Addresses|
|Stock Account Change Product Valuation|
|Stock Account Quant merge|
|Stock available lots expired|
|Stock Available Unreserved|
|Stock bar code reader|
|Stock Cancel|
|Stock Cancel delivery|
|Stock Change Price At Date|
|Stock Change Quantity Reason|
|Stock Cycle Count|
|Stock Cycle Count|
|Stock Cycle Count|
|Stock Cycle Count|
|Stock Cycle Count|
|Stock Cycle Count Rules|
|Stock Cycle Counts|
|Stock Cycle Counts Rules|
|Stock Delivery Internal|
|Stock Demand Estimate|
|Stock Disallow Negative|
|Stock Dropshipping Dual Invoice|
|Stock for this Product that must be removed from the stock. This stock is no more available for sale to Customers.
This quantity include all the production lots with a past removal date.|
|Stock for this Product that must be removed from the stock. This stock is no more available for sale to Customers.
This quantity include all the production lots with a past removal date.|
|Stock for this Product that must be removed from the stock. This stock is no more available for sale to Customers.
This quantity include all the production lots with a past removal date.|
|Stock History|
|Stock Inventory Account Manual Adjustment|
|Stock Inventory Chatter|
|Stock Inventory Discrepancy|
|Stock Inventory Exclude Sublocation|
|Stock Inventory Revaluation|
|Stock Inventory Revaluation|
|Stock Inventory Revaluation|
|Stock Inventory Revaluation|
|Stock Inventory Revaluation|
|Stock Inventory Revaluation Line Quants|
|Stock Inventory Revaluation Quants|
|Stock Inventory Sequence|
|Stock Inventory Verification Request|
|Stock level won't take into account lots expired|
|Stock Location Area Data|
|Stock Location Area Management|
|Stock Location Lockdown|
|Stock Location Ownership|
|Stock Location Restrict Procurement Group|
|Stock Logistics|
|stock lot sale tracking|
|Stock Lot Sale Tracking report|
|Stock Move Backdating|
|Stock move description|
|Stock Moves Involved|
|Stock Moves related to the given location and product.|
|Stock MTS+MTO Rule|
|Stock obsolete|
|Stock On Hand (Unreserved)|
|Stock On Hold Status|
|Stock Operation Package Mandatory|
|Stock optional valuation|
|Stock Orderpoint Automatic Creation|
|Stock Orderpoint Manual Procurement|
|Stock Orderpoint Manual Procurement UoM|
|Stock Orderpoint UoM|
|Stock Ownership Availability Rules|
|Stock Ownership By Move|
|Stock Pack Operation Auto Fill|
|Stock Packaging Usability|
|Stock Packaging Usability UL|
|Stock Picking Compute Delivery Date|
|Stock Picking Customer Ref|
|Stock Picking Deliver UOS|
|Stock picking filter lot|
|Stock Picking Invoice Link|
|Stock picking lines with sequence number|
|Stock Picking Mass Action|
|Stock Picking Mass Action|
|Stock Picking Operation Quick Change|
|Stock Picking Package Preparation|
|Stock Picking Package Preparation Line|
|Stock Picking Partner Language|
|Stock Picking Show Backorder|
|Stock Pickup Request|
|Stock Pickup Requests|
|Stock Product Category Tracked|
|Stock Product Location Sorted by Quantity|
|Stock Quant Reserved Qty UoM|
|Stock Removal Location by Priority|
|Stock Reservation|
|Stock Reservation|
|Stock Reservations|
|Stock Reservations|
|Stock Reservations|
|Stock Reservations|
|Stock Reservations|
|Stock Reservations|
|Stock Reservations|
|Stock reservations on products|
|Stock Reserve Sales|
|Stock Routes Transit|
|Stock Scanner|
|Stock Scanner Inventory|
|Stock Scanner Receipt|
|Stock Scrap Expired|
|Stock Scrap Expired|
|Stock Scrap Expired|
|Stock scrap expired id|
|Stock Scrap Expired Line|
|Stock scrap expired line ids|
|Stock Slot Verification Request|
|Stock Slot Verification Request|
|Stock Slot Verification Request|
|Stock tracking add moves|
|Stock tracking add or remove object|
|Stock tracking add packs|
|Stock Tracking Child|
|Stock Tracking extended|
|Stock Tracking Prodlot|
|Stock tracking Re-open|
|Stock Tracking Split|
|Stock Tracking State|
|Stock tracking swap|
|Stock tracking swap|
|Stock Transfer Split Multi|
|Stock Valuation Account Manual Adjustment|
|Stock Valuation Account Manual Adjustment|
|Stock Valuation Account Manual Adjustment|
|Stock Valuation Account Manual Adjustment|
|Stock Valuation Account Manual Adjustment|
|Stock Valuation Account Manual Adjustment|
|Stock Valuation Account Manual Adjustments|
|Stock Valuation Account Manual Adjustments|
|Stock Valued Picking Report|
|Stock Valued Picking Report Triple Discount|
|Stock Warehouse Orderpoint Stock Info|
|Stock Warehouse Orderpoint Stock Info Unreserved|
|Store different notes, date and title for modification, etc...|
|Temp value 1|
|Temp value 2|
|Temp value 3|
|Temp value 4|
|Temp value 5|
|Template File|
|Temporary char value.|
|Temporary char value.|
|Temporary char value.|
|Temporary char value.|
|Temporary char value.|
|Temporary float value.|
|Temporary float value.|
|Temporary float value.|
|Temporary float value.|
|Temporary float value.|
|Temporary int value.|
|Temporary int value.|
|Temporary int value.|
|Temporary int value.|
|Temporary int value.|
|Temporary text value.|
|Temporary value for scenario|
|Temporary value.|
|Temporary value.|
|Temporary value.|
|Temporary value.|
|Temporary value.|
|Temporary values|
|Terminate receipt|
|test-workflow|
|The 'act' variable must be a single character string.|
|The chosen date should be today or in the past!|
|The date used to create account moves. If empty, assumes today.Cannot be a date in the future.|
|The destination location (%s) is restricted to operation for the procurement group %s.Please choose another destination.|
|The destination location is restricted to another move!|
|The destination location is restricted to another operation!|
|The difference between the actual qty counted and the theoretical quantity on hand.|
|The discrepancy expressed in percent with theoretical quantity as basis|
|The feature might not be supported for every video type|
|The found valuation amount for product %s is zero. Which means there is probably a configuration error. Check the costing method and the standard price|
|The id of a %s cannot be empty!|
|The location '%s' is not configured to receive stock.|
|The new value for product %s cannot be negative|
|The new value for product %s cannot be negative|
|The ordered quantity has been decreased. Do not forget to take it into account on your bills and receipts.|
|The package has not been generated.|
|The pick is already validated|
|The picking has been re-opened and set to draft state|
|The Qty Update is over the Discrepancy Threshold. Please, contact a user with rights to perform this action.|
|The 'res' variable can contain multiple values :|
|The transition is followed only if this condition is evaluated as True.|
|the user will be able to manage his own human resources stuff (leave request, timesheets, ...), if he is linked to an employee in the system.|
|The 'val' variable can contain multiple values :|
|The weight is computed when the preparation is done.|
|There is a duplicate location by put away assignment!|
|There is a duplicate location by put away assignment!|
|This addon allows to retrieve all customer deliveries impacted by a lot|
|This button will automatically fill all operations that have no tracking set on the product, no processed qty and no selected package.|
|This client is specific to the stock_scanner module.|
|This lot doesn't contain any quant in internal location.|
|This menu allow you to prepare and reserve some quantities            of products.|
|This module adds a button in Production Lot/Serial Number view form to Scrap all products contained.|
|This module allows you to bring back a completed stock picking to draft state|
|This module displays the sale reference/description in the pickings|
|This module makes the product customer code visible in the stock moves of a picking.|
|This priority applies when removing stock and incoming dates are equal.|
|This priority applies when removing stock and incoming dates are equal.|
|This scenario|
|This scenario|
|This scenario will explain all step types.|
|This scenario will explain some features of the sentinel ncurses client.|
|This step allows the user to enter custom text.|
|This step allows the user to send float quantities.|
|This step allows the user to send integer numbers.|
|This step shows an error message, using the error colors defined in the hardware configuration.|
|This step waits for a confirmation from the user.|
|This text is copied to the journal entry.|
|This text is copied to the journal entry.|
|This will scrap the whole lot. Are you sure you want to continue?|
|Threshold (%)|
|time, datetime, timezone: Python module|
|Tmp values|
|To create a new work center, Go to <b><i> Master Data/Work Centers. </i></b>|
|To create expenses by email, take photos of your                             receipts and send them by email with the following                            information:|
|Tracer|
|Transaction Authorization is not supported by this payment provider.|
|Transition executed during this history line.|
|Transition for scenario|
|Transition Type|
|Transitions which goes to the next step.|
|Transitions which goes to this step.|
|Transport Information|
|Transport Information|
|Turnover Inventory Value Threshold|
|Type in a reason for the product quantity change|
|Type of rule|
|Type of transition.|
|Unknown location %s !|
|Unknown location %s!|
|Unknown product %s|
|Unknown receipt %s!|
|Unreserved|
|Unreserved|
|Unreserved stock quantity|
|Unreserved:|
|UoM : %s|
|Use MTO+MTS rules|
|Use 'Removal Priority' in Locations|
|Use uom in package|
|Used to determine fron which transition we arrive to the destination step.|
|Used to specify lot when line is created using package preparation|
|Validate All inventory Adjustments|
|Validate Inventory Adjustments Under Threshold|
|Valuation Decrease Account|
|Valuation Decrease Contra-Account|
|Valuation Decrease Contra-Account|
|Valuation discrepancy|
|Valuation discrepancy|
|Valuation discrepancy|
|Valuation Discrepancy|
|Valuation Increase Account|
|Valuation Increase Contra-Account|
|Valuation Increase Contra-Account|
|Value Turnover|
|Valued picking|
|Valued picking|
|Valued picking|
|Values id|
|Values used for this scanner.|
|Values used for this scenario.|
|Vendor Refund|
|View Invoice|
|View Reservation Move|
|Voucher Arrange|
|Waiting Actions|
|Want to manage your employee expenses and receipts? <i>Start here</i>.|
|Warehouse where is located this hardware.|
|Warehouses for this scenario.|
|Warehouses where applied|
|Webkit|
|Welcome on the stock_scanner module.|
|Width of the terminal's screen.|
|Will determine if the next work order will be planned after the previous one or after the first Quantity To Process of the previous one.|
|Write a python expression, beginning with record, that gives the record to update. An expression builder is available in the help tab. Examples:|
|You are authenticated as %s !|
|You are now authenticated as %s !|
|You are now logged out|
|You can apply the cycle count rules in complete                        warehouses or specific zones. A zone it is                        understood as a location and all its children.|
|You can change destination location in operations.                    <br/>|
|You can not change operations destination location if picking state not is in %s|
|You can not process an actual movement date in the future.|
|You can not re-open a period which belongs to closed fiscal year|
|You can only confirm cycle counts in state 'Planned'.|
|You can only have one zero confirmation rule per warehouse.|
|You can only post quant cost changes.|
|You can select which partners have valued pickings|
|You can select which partners have valued pickings|
|You can select which partners have valued pickings|
|You can set an optionnal <strong class=""text-primary"">PRICE</strong>                            at the end of the subject of your email.|
|You can set to draft cancelled moves only|
|You cannot change destination location if any move has a destination move.|
|You cannot define a negative or null number of counts per period.|
|You cannot define a negative period.|
|You cannot have a positive and negative amounts on the same expense report.|
|You cannot have a positive and negative amounts on the same expense report.|
|You cannot modify the configuration of an Inventory Adjustment related to a Cycle Count.|
|You cannot remove the journal entry that is related to a Stock valuation account manual adjustment |
|You cannot remove the journal item that is related to a Stock valuation account manual adjustment |
|You cannot remove the journal item that is related to an inventory revaluation|
|You cannot remove the journal item that is related to an inventory revaluation|
|You cannot scrap a move without having available stock for %s. You can correct it with an inventory adjustment.|
|You cannot use the same serial number in two different lines.|
|You cannot validate this stock operation because the stock level of the product '%s'%s would become negative (%s) on the stock location '%s' and negative stock is not allowed for this product.|
|You haven't set processed (<i>done</i>) quantities. Click <i>apply</i> and                        Odoo will process all quantities to do.|
|You must enter a lot for this product!|
|You must enter done quantity in order to split your picking in several ones.|
|You need to provide a Lot/Serial Number for product %s|
|You will also use this step for barcode scanning.|
|Your Expense %s has been refused.<br/><ul class=o_timeline_tracking_value_list><li>Reason<span> : </span><spanclass=o_timeline_tracking_value>%s</span></li></ul>|
|Zero Confirmation|
|Zero confirmation rules can only have one warehouse assigned.|
